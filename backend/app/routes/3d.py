"""3D configurator routes.

Deterministic stubs: no real mesh generation. Task ids are encoded and echoed
back by /status so the frontend contract works end to end.
"""
from __future__ import annotations

import base64
import json
from typing import Any, Dict, List, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.celery_app import celery_app
from app.services.task_store import task_store

router = APIRouter(prefix="/api/v1/3d", tags=["3d"])


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


class GenerateRequest(BaseModel):
    """JSON form of the spec's multipart body (python-multipart is not installed)."""

    vehicle_brand: str = Field(..., min_length=1, max_length=100)
    vehicle_model: str = Field(..., min_length=1, max_length=100)
    images: Optional[List[str]] = Field(None, description="Photo URLs or base64 payloads, max 4")


class Modification(BaseModel):
    component_type: str
    part_id: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


class ModifyRequest(BaseModel):
    base_mesh_id: str
    modifications: List[Modification] = Field(..., min_length=1)


@router.post("/generate", status_code=status.HTTP_202_ACCEPTED)
def generate(payload: GenerateRequest) -> dict:
    """Queue a (stub) 3D reconstruction task via Celery."""
    if payload.images and len(payload.images) > 4:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Maksimal 4 foto")

    record = task_store.create()
    image_urls = payload.images or []

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

    return {
        "task_id": record.task_id,
        "status": record.status,
        "mesh_url": record.mesh_url,
        "texture_url": record.texture_url,
        "error": record.error,
    }


@router.post("/modify")
def modify(payload: ModifyRequest) -> dict:
    """Apply (stub) component modifications to a base mesh."""
    return {
        "modified_mesh_url": f"https://cdn.otomotif-ai.com/meshes/{payload.base_mesh_id}-mod.glb",
        "modification_id": str(uuid4()),
        "affiliate_links": [
            {
                "part_id": m.part_id,
                "shopee_affiliate_link": f"https://shp.ee/{m.part_id[:8]}",
            }
            for m in payload.modifications
        ],
    }
