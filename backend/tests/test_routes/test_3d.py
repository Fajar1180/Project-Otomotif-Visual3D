"""Integration tests for 3D generation /status endpoints (issue #5)."""
import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_generate_rejects_more_than_four_images():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/3d/generate",
            json={"vehicle_brand": "Toyota", "vehicle_model": "Avanza", "images": ["a"] * 5},
        )
    assert resp.status_code == 422, resp.text


@pytest.mark.asyncio
async def test_generate_returns_task_id_and_status_processing():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/3d/generate",
            json={
                "vehicle_brand": "Toyota",
                "vehicle_model": "Avanza",
                "images": ["https://example.com/1.jpg", "https://example.com/2.jpg"],
            },
        )
    assert resp.status_code == 202, resp.text
    body = resp.json()
    assert "task_id" in body
    assert body["status"] == "processing"
    return body["task_id"]


@pytest.mark.asyncio
async def test_status_unknown_task_returns_404():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/api/v1/3d/status/does-not-exist")
    assert resp.status_code == 404, resp.text
    assert resp.json()["error"] == "NOT_FOUND"


@pytest.mark.asyncio
async def test_status_returns_record_after_generate():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        gen = await client.post(
            "/api/v1/3d/generate",
            json={
                "vehicle_brand": "Honda",
                "vehicle_model": "Beat",
                "images": ["https://example.com/1.jpg"],
            },
        )
        assert gen.status_code == 202, gen.text
        task_id = gen.json()["task_id"]

        resp = await client.get(f"/api/v1/3d/status/{task_id}")
        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body["task_id"] == task_id
        assert body["status"].lower() in {"processing", "completed", "failed"}
        if body["status"] == "failed":
            assert body["error"] is not None
