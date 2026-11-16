"""Celery task: generate 3D mesh from 4 input images (placeholder pipeline)."""
from __future__ import annotations

from app.celery_app import celery_app
from app.services.task_store import task_store

# ponytail: real pipeline (mesh/texture synthesis) is stubbed here.
# Ceiling: swap _synthesize for a genuine 3D reconstruction service.
# Upgrade path: implement _synthesize, then wire store updates to result URLs.


def _synthesize(image_urls: list[str]) -> tuple[str, str]:
    """Stub: return fake mesh/texture URLs."""
    import time

    time.sleep(0.1)  # simulate work
    return "https://cdn.example.com/mesh.obj", "https://cdn.example.com/texture.png"


@celery_app.task(name="app.tasks.three_d.generate_3d", bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 2})
def generate_3d(self, task_id: str, image_urls: list[str]) -> dict:
    record = task_store.get(task_id)
    if not record:
        return {"status": "not_found", "task_id": task_id}

    task_store.update(task_id, status="PROCESSING")
    try:
        mesh_url, texture_url = _synthesize(image_urls)
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
