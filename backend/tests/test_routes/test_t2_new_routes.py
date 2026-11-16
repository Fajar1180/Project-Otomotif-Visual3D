"""Smoke tests for T2 routes: vehicles, workshops, 3d, diagnosis history."""
from __future__ import annotations

from typing import Any, Dict

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import text

from app.database import SessionLocal
from app.main import app
from models import DiagnosticResult


def _seed_workshop() -> None:
    db = SessionLocal()
    try:
        db.execute(
            text(
                "INSERT INTO workshops (id, name, address, latitude, longitude, phone, specialties, rating) "
                "VALUES ('ws-111', 'Bengkel Coba', 'Jl. Coba', -6.2, 106.8, '021', '[\"matic\"]', 4.5)"
            )
        )
        db.commit()
    finally:
        db.close()


def _seed_history() -> None:
    db = SessionLocal()
    try:
        db.add(
            DiagnosticResult(
                symptom_text="mobil tidak bisa nyala",
                diagnosis="Aki habis",
                severity="DIY_EASY",
                confidence_score=0.9,
                repair_steps=[{"step": 1, "description": "Charge aki"}],
            )
        )
        db.commit()
    finally:
        db.close()


@pytest.mark.asyncio
async def test_vehicles(test_db_async):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        r = await client.post(
            "/api/v1/vehicles",
            json={"brand": "Honda", "model": "Vario 150", "year_start": 2015, "category": "matic"},
        )
        assert r.status_code == 201, r.text
        vid: str = r.json()["id"]

        r = await client.get(f"/api/v1/vehicles/{vid}")
        assert r.status_code == 200
        assert r.json()["brand"] == "Honda"

        r = await client.get(
            "/api/v1/vehicles", params={"brand": "Honda", "page": 1, "limit": 10}
        )
        assert r.status_code == 200
        assert r.json()["meta"]["total"] >= 1

        r = await client.get("/api/v1/vehicles/nope-uuid")
        assert r.status_code == 404


@pytest.mark.asyncio
async def test_workshops(test_db_async):
    _seed_workshop()
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        r = await client.get("/api/v1/workshops", params={"lat": -6.2, "lng": 106.8})
        assert r.status_code == 200
        assert r.json()["meta"]["total"] >= 1
        assert r.json()["data"][0]["distance_km"] == 0.0

        r = await client.get("/api/v1/workshops", params={"specialty": "matic"})
        assert r.status_code == 200
        assert all("matic" in (w["specialties"] or []) for w in r.json()["data"])

        r = await client.get("/api/v1/workshops/ws-111")
        assert r.status_code == 200
        assert r.json()["name"] == "Bengkel Coba"

        r = await client.get("/api/v1/workshops/nope")
        assert r.status_code == 404


@pytest.mark.asyncio
async def test_3d(test_db_async):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        r = await client.post(
            "/api/v1/3d/generate",
            json={
                "vehicle_brand": "Honda",
                "vehicle_model": "Vario 150",
                "images": ["http://x/f1.jpg"],
            },
        )
        assert r.status_code == 202, r.text
        task_id: str = r.json()["task_id"]
        assert r.json()["status"] == "processing"

        r = await client.get(f"/api/v1/3d/status/{task_id}")
        assert r.status_code == 200
        assert r.json()["status"].lower() == "completed"
        assert r.json()["task_id"] == task_id

        r = await client.get("/api/v1/3d/status/nope-task")
        assert r.status_code == 404

        r = await client.post(
            "/api/v1/3d/modify",
            json={
                "base_mesh_id": "mesh-1",
                "modifications": [
                    {"component_type": "wheels", "part_id": "p-1", "parameters": {"size": 17}}
                ],
            },
        )
        assert r.status_code == 200
        assert "modified_mesh_url" in r.json()
        assert len(r.json()["affiliate_links"]) == 1


@pytest.mark.asyncio
async def test_diagnosis_history(test_db_async):
    _seed_history()
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        r = await client.get("/api/v1/diagnosis/history")
        assert r.status_code == 200, r.text
        bodies = r.json()["data"]
        assert r.json()["meta"]["total"] >= 1
        assert any(b["conclusion"] == "Aki habis" for b in bodies)

        r = await client.get("/api/v1/diagnosis/history", params={"severity": "DIY_EASY"})
        assert r.status_code == 200
        assert r.json()["meta"]["total"] >= 1

        r = await client.get(
            "/api/v1/diagnosis/history", params={"severity": "WORKSHOP_REQUIRED"}
        )
        assert r.status_code == 200
        assert r.json()["meta"]["total"] == 0
