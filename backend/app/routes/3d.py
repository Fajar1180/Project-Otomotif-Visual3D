"""3D configurator routes.

Deterministic stubs: no real mesh generation. Task ids are encoded and echoed
back by /status so the frontend contract works end to end.
"""
from __future__ import annotations

import base64
import json
import os
from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status, UploadFile, File, Form
from pydantic import BaseModel, Field

from app.celery_app import celery_app
from app.services.task_store import task_store
from config import settings

router = APIRouter(prefix="/api/v1/3d", tags=["3d"])

MAX_PHOTOS = 4
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB per file
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}

OUTPUT_DIR = settings.THREE_D_OUTPUT_DIR


def _encode_task(brand: str, model: str) -> str:
    raw = json.dumps({"b": brand, "m": model}).encode()
    return "task_" + base64.urlsafe_b64encode(raw).decode().rstrip("=")


def _decode_task(task_id: str) -> Dict[str, str]:
    try:
        padded = task_id.removeprefix("task_") + "=" * (-(len(task_id) - 5) % 4)
        data = json.loads(base64.urlsafe_b64decode(padded))
        return {"brand": data["b"], "model": data["m"]}
    except Exception:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Task tidak ditemukan")


class Modification(BaseModel):
    component_type: str
    part_id: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


class ModifyRequest(BaseModel):
    base_mesh_id: str
    modifications: List[Modification] = Field(..., min_length=1)


@router.post("/generate", status_code=status.HTTP_202_ACCEPTED)
async def generate(
    vehicle_brand: str = Form(...),
    vehicle_model: str = Form(...),
    images: List[UploadFile] = File(...),
) -> dict:
    """Queue a 3D reconstruction task from 4 vehicle photos (multipart)."""
    if not vehicle_brand.strip() or not vehicle_model.strip():
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Brand dan model wajib diisi")
    if len(images) != MAX_PHOTOS:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"Harus tepat {MAX_PHOTOS} foto (front, back, left, right), diterima {len(images)}",
        )
    
    # Validate image size and MIME type
    for img in images:
        # Read a preview to check size without loading entire file
        content = await img.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status.HTTP_413_PAYLOAD_TOO_LARGE,
                f"File {img.filename} terlalu besar (maksimal {MAX_FILE_SIZE // (1024*1024)}MB)",
            )
        if img.content_type not in ALLOWED_MIME_TYPES:
            raise HTTPException(
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                f"Tipe file {img.filename} tidak didukung. Hanya: {', '.join(ALLOWED_MIME_TYPES)}",
            )
        # Reset file pointer after reading for Celery task
        img.file.seek(0)
    
    record = task_store.create()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image_urls = []
    for img in images:
        img.file.seek(0)
        dst = os.path.join(OUTPUT_DIR, f"{record.task_id}_{img.filename}")
        with open(dst, "wb") as f:
            f.write(await img.read())
        image_urls.append(dst)

    if celery_app.conf.task_always_eager:
        from app.tasks.three_d import generate_3d

        generate_3d.apply(args=[record.task_id, image_urls])
    else:
        celery_app.send_task(
            "app.tasks.three_d.generate_3d",
            args=[record.task_id, image_urls],
        )

    return {
        "task_id": record.task_id,
        "status": "processing",
        "message": "Konstruksi 3D berjalan di background",
        "estimated_time_seconds": 120,
    }


@router.get("/status/{task_id}")
def task_status(task_id: str) -> dict:
    """Report the status of a generate task."""
    record = task_store.get(task_id)
    if not record:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Task tidak ditemukan")

    # Expose a URL that the frontend can load, not a raw filesystem path.
    mesh = record.mesh_url or ""
    if mesh and not mesh.startswith("http"):
        mesh = f"/static/meshes/{os.path.basename(mesh)}"
    texture = record.texture_url or ""
    if texture and not texture.startswith("http"):
        texture = f"/static/meshes/{os.path.basename(texture)}"

    return {
        "task_id": record.task_id,
        "status": record.status,
        "mesh_url": mesh,
        "texture_url": texture,
        "error": record.error,
    }


@router.post("/modify")
def modify(payload: ModifyRequest) -> dict:
    """Apply (stub) component modifications to a base mesh."""
    # Sanitize part_id: only alphanumeric characters, max 8 chars for affiliate link
    safe_part_ids = []
    for m in payload.modifications:
        # Keep only alphanumeric characters
        sanitized = "".join(c for c in m.part_id if c.isalnum())[:8]
        safe_part_ids.append(sanitized)
    
    return {
        "modified_mesh_url": f"https://cdn.otomotif-ai.com/meshes/{payload.base_mesh_id}-mod.glb",
        "modification_id": str(uuid4()),
        "affiliate_links": [
            {
                "part_id": m.part_id,
                "shopee_affiliate_link": f"https://shp.ee/{safe_part_id}",
            }
            for m, safe_part_id in zip(payload.modifications, safe_part_ids)
        ],
    }
