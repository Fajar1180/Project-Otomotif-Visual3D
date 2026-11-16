"""Celery application for background 3D mesh generation tasks.

Broker/backend: Redis (settings.redis_url). Falls back to eager mode when
celery_task_always_eager is True (tests / local dev without a worker).
"""
from __future__ import annotations

from celery import Celery
from config import settings

celery_app = Celery(
    "otomotif_ai",
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=["app.tasks.three_d"],
)

celery_app.conf.update(
    task_always_eager=settings.celery_task_always_eager,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    result_expires=3600,
)

__all__ = ["celery_app"]
