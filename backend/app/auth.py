"""Password hashing and JWT (HS256) helpers.

No extra dependency: signed tokens use stdlib hmac/hashlib. Passwords use
passlib+bcrypt when importable, else stdlib pbkdf2_hmac.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
from typing import Any, Dict, Optional
from uuid import uuid4

from config import (
    JWT_SECRET,
    JWT_EXPIRE_MINUTES,
    DATABASE_URL,
    REDIS_URL,
    SHOPEE_APP_ID,
    SHOPEE_APP_KEY,
    SHOPEE_APP_SECRET,
)

try:  # bcrypt is installed in the venv; pbkdf2 is the stdlib fallback
    import bcrypt as _bcrypt

    def hash_password(password: str) -> str:
        # bcrypt silently truncates past 72 bytes; cut explicitly.
        return _bcrypt.hashpw(password.encode()[:72], _bcrypt.gensalt()).decode()

    def verify_password(password: str, hashed: str) -> bool:
        try:
            return _bcrypt.checkpw(password.encode()[:72], hashed.encode())
        except ValueError:
            return False

except ImportError:  # pragma: no cover
    _ITERATIONS = 200_000

    def hash_password(password: str) -> str:
        salt = os.urandom(16)
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, _ITERATIONS)
        return f"pbkdf2_sha256${_ITERATIONS}${salt.hex()}${digest.hex()}"

    def verify_password(password: str, hashed: str) -> bool:
        try:
            _, iterations, salt_hex, digest_hex = hashed.split("$")
            digest = hashlib.pbkdf2_hmac(
                "sha256", password.encode(), bytes.fromhex(salt_hex), int(iterations)
            )
            return hmac.compare_digest(digest.hex(), digest_hex)
        except ValueError:
            return False

def _b64e(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def _b64d(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _sign(signing_input: str) -> str:
    return _b64e(
        hmac.new(JWT_SECRET.encode(), signing_input.encode(), hashlib.sha256).digest()
    )


def create_access_token(subject: str, expires_minutes: Optional[int] = None) -> str:
    """Return a signed HS256 JWT for ``subject`` (usually the user id)."""
    now = int(time.time())
    ttl = (expires_minutes or JWT_EXPIRE_MINUTES) * 60
    header = _b64e(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    payload = _b64e(
        json.dumps({"sub": str(subject), "iat": now, "exp": now + ttl}, separators=(",", ":")).encode()
    )
    signing_input = f"{header}.{payload}"
    return f"{signing_input}.{_sign(signing_input)}"


def create_refresh_token(subject: str, expires_days: int = 7) -> str:
    """Return a long-lived signed HS256 JWT refresh token for ``subject``."""
    now = int(time.time())
    ttl = expires_days * 86400
    header = _b64e(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    payload = _b64e(
        json.dumps(
            {"sub": str(subject), "iat": now, "typ": "refresh", "jti": str(uuid4()), "exp": now + ttl},
            separators=(",", ":"),
        ).encode()
    )
    signing_input = f"{header}.{payload}"
    return f"{signing_input}.{_sign(signing_input)}"


def decode_access_token(token: str) -> Dict[str, Any]:
    """Verify signature + expiry; raise ValueError on any failure."""
    try:
        header, payload, signature = token.split(".")
    except ValueError:
        raise ValueError("Malformed token")
    if not hmac.compare_digest(signature, _sign(f"{header}.{payload}")):
        raise ValueError("Invalid signature")
    data = json.loads(_b64d(payload))
    if int(data.get("exp", 0)) < int(time.time()):
        raise ValueError("Token expired")
    return data


def get_current_user(token: str) -> Dict[str, Any]:
    """Dependency: decode JWT and return user payload dict.

    Raises ValueError if token is invalid or expired.
    The caller (route) should catch this and return 401.
    """
    return decode_access_token(token)
