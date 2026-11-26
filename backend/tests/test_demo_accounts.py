"""Demo/dummy account login + 3D generate without Redis.

Relies on conftest autouse fixture `_celery_eager_for_tests` (task_always_eager=True)
so Celery 3D tasks run synchronously — no Redis worker/broker required.
"""
from httpx import ASGITransport, AsyncClient

import pytest

from app.main import app
from seed.seed_auth import ACCOUNTS as DEMO_ACCOUNTS  # single source of truth


async def _post_json(client: AsyncClient, path: str, payload: dict):
    return await client.post(path, json=payload)


@pytest.mark.asyncio
async def test_demo_user_login(test_db_async):
    from seed.seed_auth import seed_auth
    seed_auth(test_db_async)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        for acct in DEMO_ACCOUNTS:
            resp = await _post_json(
                client,
                "/api/v1/auth/login",
                {"email": acct["email"], "password": acct["password"]},
            )
            assert resp.status_code == 200, f"{acct['role']} login failed: {resp.text}"
            body = resp.json()
            assert body["access_token"]
            assert body["user"]["email"] == acct["email"]


@pytest.mark.asyncio
async def test_demo_login_wrong_password_rejected(test_db_async):
    from seed.seed_auth import seed_auth
    seed_auth(test_db_async)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await _post_json(
            client,
            "/api/v1/auth/login",
            {"email": "user@otomotif.ai", "password": "salahbanget"},
        )
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_3d_generate_without_redis(test_db_async):
    """3D generate returns 202 + task_id and status completes (celery eager, no Redis)."""
    import io

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        gen = await client.post(
            "/api/v1/3d/generate",
            data={"vehicle_brand": "Honda", "vehicle_model": "Beat"},
            files=[
                ("images", (f"f{i}.jpg", io.BytesIO(b"\xff\xd8\xff"), "image/jpeg"))
                for i in range(4)
            ],
        )
    assert gen.status_code == 202, gen.text
    task_id = gen.json()["task_id"]
    assert gen.json()["status"] == "processing"

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get(f"/api/v1/3d/status/{task_id}")
    assert resp.status_code == 200, resp.text
    assert resp.json()["task_id"] == task_id
    assert resp.json()["status"].lower() in {"processing", "completed", "failed"}
