"""Pytest configuration and fixtures."""
import os
import pytest
import pytest_asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.celery_app import celery_app
from app.database import SessionLocal, Base, _engine, get_db
from models import Vehicle, Symptom, Diagnosis, SparePart, DiagnosisPartMap, VectorStore, Workshop, DiagnosticResult


@pytest.fixture(scope="session")
def test_db_engine():
    """Create test database engine (SQLite in-memory)."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_db(test_db_engine):
    """Provide a test database session."""
    TestSessionLocal = sessionmaker(bind=test_db_engine)
    session = TestSessionLocal()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="session", autouse=True)
def _ensure_test_schema():
    """Create all tables once on the app engine so route tests see them."""
    Base.metadata.create_all(bind=_engine)

import app.routes.auth as auth_routes

@pytest.fixture(autouse=True)
def _reset_login_rate_limit():
    """Reset in-memory login rate limiter so tests don't collide on shared IP."""
    auth_routes._login_hits = {}

@pytest_asyncio.fixture
async def test_db_async():
    """Provide a test database session bound to the app engine (so seeded data is visible to routes)."""
    session = SessionLocal()

    def _override_get_db():
        yield session

    app.dependency_overrides[get_db] = _override_get_db
    try:
        yield session
    finally:
        app.dependency_overrides.pop(get_db, None)
        session.rollback()
        session.close()


@pytest.fixture(autouse=True)
def _celery_eager_for_tests():
    """Run Celery tasks synchronously in tests (no Redis/worker needed)."""
    celery_app.conf.task_always_eager = True
    yield
    celery_app.conf.task_always_eager = False
