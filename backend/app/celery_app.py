"""Celery application for background 3D mesh generation tasks.

Broker/backend: Redis (settings.redis_url). Falls back to eager mode when
celery_task_always_eager is True (tests / local dev without a worker).

Windows dev note: without Redis at localhost:6379, set CELERY_ALWAYS_EAGER=true
(default here) so tasks run inline and Celery never dials the broker (no
10061 connection-refused errors). When running a real worker on Windows, use:

    celery -A app.celery_app worker --pool=solo

--pool=solo avoids the Windows-incompatible prefork pool and processes tasks
inline in the worker process.
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
