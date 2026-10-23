"""Database configuration and session management.

Async engine + async session generator for FastAPI routes.
Single declarative Base lives in models.py.
"""

from __future__ import annotations

import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool

from config import settings
from models import Base  # noqa: F401 — registers all models on Base.metadata


def _async_url(url: str) -> str:
    """Translate sync DSN to async driver DSN."""
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)
    if url.startswith("sqlite://"):
        return url.replace("sqlite://", "sqlite+aiosqlite://", 1)
    return url


_url = _async_url(settings.database_url)

if _url.startswith("sqlite"):
    _engine = create_async_engine(
        _url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
else:
    _engine = create_async_engine(_url, pool_pre_ping=True, future=True)

SessionLocal = async_sessionmaker(
    bind=_engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def init_db() -> None:
    """Create all tables (call once at app start)."""
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yield an AsyncSession for FastAPI's Depends(get_db)."""
    async with SessionLocal() as session:
        yield session


# ---------------------------------------------------------------------------
# Optional: echo SQL when DEBUG is enabled (SQLite only, to avoid noise in
# production logs).  Run with `SQL_ECHO=1` env var.
# ---------------------------------------------------------------------------
if os.getenv("SQL_ECHO") == "1":
    _engine.echo = True  # type: ignore[assignment]