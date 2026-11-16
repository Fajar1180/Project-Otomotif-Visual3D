"""Celery task: generate 3D mesh from 4 input images (Issue #5).

Uses the Service Adapter Pattern (app/services/three_d_engine.py) so the
engine can be swapped between ``fallback`` (local .glb generator, no GPU /
no model weights), ``replicate``, ``huggingface``, or ``external`` worker
via ``THREE_D_ENGINE`` env var — without downloading PyTorch/InstantMesh
locally.

Retry: max 3 attempts with exponential backoff. Task status tracked in
task_store.
"""

from __future__ import annotations

from typing import Optional, Tuple

from app.celery_app import celery_app
from app.services.task_store import task_store
from app.services.three_d_engine import get_engine, ThreeDEngineError


@celery_app.task(
    name="app.tasks.three_d.generate_3d",
    bind=True,
    autoretry_for=(ThreeDEngineError, Exception),
    retry_kwargs={"max_retries": 3, "countdown": 2, "backoff": 2},
)
def generate_3d(self, task_id: str, image_urls: list[str]) -> dict:
    record = task_store.get(task_id)
    if not record:
        return {"status": "not_found", "task_id": task_id}

    task_store.update(task_id, status="PROCESSING")
    try:
        engine = get_engine()
        mesh_url, texture_url = engine.synthesize(image_urls)
        task_store.update(
            task_id,
            status="COMPLETED",
            mesh_url=mesh_url,
            texture_url=texture_url,
        )
        return {"status": "completed", "task_id": task_id}
    except Exception as exc:  # noqa: BLE001
        task_store.update(task_id, status="FAILED", error=str(exc))
        raise self.retry(exc=exc)
