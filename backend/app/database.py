"""Database configuration and session management.

Single declarative Base, async/sync-aware get_db generator.
"""

from __future__ import annotations

import os
from typing import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session as SA_Session, sessionmaker
from sqlalchemy.pool import StaticPool

from config import settings
from models import Base  # Export Base for use in tests/routes

# ---------------------------------------------------------------------------
# Engine: SQLite (tests) or PostgreSQL (production).  For SQLite we use
# StaticPool + check_same_thread=False.  For PostgreSQL we rely on the
# DSN from settings (default: SQLite in-memory for CI/tests).
# ---------------------------------------------------------------------------
if settings.database_url.startswith("postgresql"):
    _engine = create_engine(
        settings.database_url,
        future=True,
        pool_pre_ping=True,
    )
else:
    _engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )

SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, future=True)


def init_db() -> None:
    """Create all tables (call once at app start or in test setup)."""
    Base.metadata.create_all(bind=_engine)


def get_db() -> Generator[SA_Session, None, None]:
    """Yield a SQLAlchemy session.

    Yields a session that the caller (route) must close.  In production
    this is typically wrapped by FastAPI's `Depends(get_db)` which ensures
    the session is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Optional: echo SQL when DEBUG is enabled (SQLite only, to avoid noise in
# production logs).  Run with `SQL_ECHO=1` env var.
# ---------------------------------------------------------------------------
if os.getenv("SQL_ECHO") == "1":
    _engine.echo = True  # type: ignore[assignment]