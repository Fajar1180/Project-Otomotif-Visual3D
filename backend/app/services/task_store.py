"""In-memory task status store for 3D generation tasks.

Single-process store good enough for one worker. Swap for Redis/DB when
multi-worker. Statuses: PENDING, PROCESSING, COMPLETED, FAILED.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


@dataclass
class TaskRecord:
    task_id: str
    status: str = "PENDING"
    mesh_url: Optional[str] = None
    texture_url: Optional[str] = None
    error: Optional[str] = None
    created_at: float = field(default_factory=lambda: __import__("time").time())


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[str, TaskRecord] = {}
        self._lock = threading.Lock()

    def create(self, task_id: Optional[str] = None) -> TaskRecord:
        task_id = task_id or str(uuid4())
        with self._lock:
            record = TaskRecord(task_id=task_id)
            self._tasks[task_id] = record
        return record

    def get(self, task_id: str) -> Optional[TaskRecord]:
        with self._lock:
            return self._tasks.get(task_id)

    def update(
        self,
        task_id: str,
        status: Optional[str] = None,
        mesh_url: Optional[str] = None,
        texture_url: Optional[str] = None,
        error: Optional[str] = None,
    ) -> Optional[TaskRecord]:
        with self._lock:
            record = self._tasks.get(task_id)
            if not record:
                return None
            if status is not None:
                record.status = status
            if mesh_url is not None:
                record.mesh_url = mesh_url
            if texture_url is not None:
                record.texture_url = texture_url
            if error is not None:
                record.error = error
        return record


task_store = TaskStore()

__all__ = ["TaskStore", "TaskRecord", "task_store"]
