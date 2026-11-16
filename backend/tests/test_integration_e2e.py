"""End-to-end integration tests (Issue #12).

Covers two user flows end-to-end across module boundaries:

1. Register/Login → AI Diagnosis → Workshop Finder
2. Upload 3D → Celery Task Status → Shopee Affiliate Link + Click Tracking

Uses TestClient-style AsyncClient against the real FastAPI app with
celery in eager mode (conftest already forces task_always_eager=True).
"""
import io
import uuid

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


def _files(count: int = 4):
    return [
        ("images", (f"photo{i}.jpg", io.BytesIO(b"\xff\xd8\xff"), "image/jpeg"))
        for i in range(count)
    ]


@pytest.mark.asyncio
async def test_e2e_auth_diagnosis_workshop(test_db_async):
    """Flow: register → login → diagnosis → workshop finder."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Register
        reg = await client.post(
            "/api/v1/auth/register",
            json={"email": "e2e@example.com", "password": "rahasia123", "full_name": "E2E User"},
        )
        assert reg.status_code == 201, reg.text
        token = reg.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # 2. Login (re-verify)
        login = await client.post(
            "/api/v1/auth/login",
            json={"email": "e2e@example.com", "password": "rahasia123"},
        )
        assert login.status_code == 200

        # 3. AI Diagnosis
        dia = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Engine knocking sound at high RPM and oil consumption",
                "vehicle_make": "Honda",
                "vehicle_model": "Civic",
                "vehicle_year": 2020,
            },
        )
        assert dia.status_code == 200, dia.text
        diag_body = dia.json()
        assert "diagnosis_id" in diag_body
        assert diag_body["severity_level"] in ("DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED")

        # 4. Workshop Finder
        ws = await client.get("/api/v1/workshops", params={"lat": -6.2, "lng": 106.8, "radius_km": 10})
        assert ws.status_code == 200
        ws_body = ws.json()
        assert "data" in ws_body
        assert "meta" in ws_body
        for w in ws_body["data"]:
            for f in ("id", "name", "address", "phone", "rating"):
                assert f in w, f"Missing workshop field: {f}"

        # 5. Diagnosis history audit trail
        hist = await client.get("/api/v1/diagnosis/history", headers=headers)
        assert hist.status_code == 200
        assert "data" in hist.json()


@pytest.mark.asyncio
async def test_e2e_threed_shopee_click(test_db_async):
    """Flow: upload 3D (4 photos) → task status → Shopee search + click tracking."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 1. Upload 3D with exactly 4 images
        gen = await client.post(
            "/api/v1/3d/generate",
            data={"vehicle_brand": "Toyota", "vehicle_model": "Avanza"},
            files=_files(4),
        )
        assert gen.status_code == 202, gen.text
        task_id = gen.json()["task_id"]
        assert gen.json()["status"] == "processing"

        # 2. Celery task status (eager → should be completed quickly)
        status_resp = await client.get(f"/api/v1/3d/status/{task_id}")
        assert status_resp.status_code == 200
        status_body = status_resp.json()
        assert status_body["task_id"] == task_id
        assert status_body["status"].lower() in ("processing", "completed", "failed")

        # 3. Shopee affiliate search (requires auth via get_current_user)
        # Get a token first
        reg = await client.post(
            "/api/v1/auth/register",
            json={"email": "shopee@example.com", "password": "rahasia123", "full_name": "Shopee User"},
        )
        assert reg.status_code == 201, reg.text
        token = reg.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        search = await client.post(
            "/shopee/search",
            params={"query": "brake pad", "limit": 5, "token": token},
        )
        assert search.status_code == 200, search.text
        search_body = search.json()
        assert "items" in search_body
        assert "click_tracking_id" in search_body
        for item in search_body["items"]:
            assert any(k in item for k in ("shopee_affiliate_link", "shopee_url")), f"Missing affiliate link in item: {item}"

        # 4. Click tracking via service (direct function call)
        from app.services.shopee import track_click
        click_id = track_click(f"item:{task_id}")
        assert click_id, "click tracking should return a non-empty id"
