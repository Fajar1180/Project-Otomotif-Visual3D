"""Integration tests for auth register/login."""
import pytest
from httpx import ASGITransport, AsyncClient

from app.auth import decode_access_token
from app.main import app


@pytest.mark.asyncio
async def test_register_then_login(test_db_async):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        reg = await client.post(
            "/api/v1/auth/register",
            json={"email": "user@example.com", "password": "rahasia123", "full_name": "Budi"},
        )
        assert reg.status_code == 201, reg.text
        body = reg.json()
        assert body["token_type"] == "bearer"
        assert body["user"]["email"] == "user@example.com"
        assert "hashed_password" not in body["user"]
        assert decode_access_token(body["access_token"])["sub"] == body["user"]["id"]

        dup = await client.post(
            "/api/v1/auth/register",
            json={"email": "user@example.com", "password": "rahasia123"},
        )
        assert dup.status_code == 409
        assert dup.json()["error"] == "CONFLICT"

        ok = await client.post(
            "/api/v1/auth/login",
            json={"email": "user@example.com", "password": "rahasia123"},
        )
        assert ok.status_code == 200
        assert ok.json()["access_token"]

        bad = await client.post(
            "/api/v1/auth/login",
            json={"email": "user@example.com", "password": "salahbanget"},
        )
        assert bad.status_code == 401
        assert bad.json()["error"] == "UNAUTHORIZED"
