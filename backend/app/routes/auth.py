"""Auth routes: register + login (JWT)."""
from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth import create_access_token, create_refresh_token, decode_access_token, hash_password, verify_password
from app.database import get_db
from models import RefreshToken, User

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

_LOGIN_LIMIT = 5
_LOGIN_WINDOW = 60.0
_login_hits: dict = {}


def _login_rate_limit(request: Request) -> None:
    """In-memory rate limit for login attempts per IP (5 / 60s)."""
    ip = request.client.host if request.client else "unknown"
    now = time.monotonic()
    start, count = _login_hits.get(ip, (now, 0))
    if now - start >= _LOGIN_WINDOW:
        start, count = now, 0
    count += 1
    _login_hits[ip] = (start, count)
    if count > _LOGIN_LIMIT:
        retry_after = max(1, int(_LOGIN_WINDOW - (now - start)))
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={
                "error": "RATE_LIMITED",
                "message": "Terlalu banyak percobaan login, coba lagi nanti",
                "retry_after": retry_after,
            },
        )


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    full_name: Optional[str] = Field(None, max_length=150)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    created_at: Optional[datetime] = None


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserOut


class RefreshRequest(BaseModel):
    refresh_token: str


class RefreshResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) -> TokenResponse:
    """Create an account and return an access token."""
    exists = db.execute(select(User).where(User.email == payload.email)).scalar_one_or_none()
    if exists:
        raise HTTPException(status.HTTP_409_CONFLICT, "Email sudah terdaftar")

    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.full_name,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    refresh_token = create_refresh_token(str(user.id))
    db.add(
        RefreshToken(
            user_id=str(user.id),
            token=refresh_token,
            expires_at=datetime.now(timezone.utc) + timedelta(days=7),
        )
    )
    db.commit()
    return TokenResponse(
        access_token=create_access_token(str(user.id)),
        refresh_token=refresh_token,
        user=UserOut.model_validate(user, from_attributes=True),
    )


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, request: Request, db: Session = Depends(get_db)) -> TokenResponse:
    """Exchange email + password for an access token."""
    _login_rate_limit(request)
    user = db.execute(select(User).where(User.email == payload.email)).scalar_one_or_none()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Email atau password salah")
    refresh_token = create_refresh_token(str(user.id))
    db.add(
        RefreshToken(
            user_id=str(user.id),
            token=refresh_token,
            expires_at=datetime.now(timezone.utc) + timedelta(days=7),
        )
    )
    db.commit()
    return TokenResponse(
        access_token=create_access_token(str(user.id)),
        refresh_token=refresh_token,
        user=UserOut.model_validate(user, from_attributes=True),
    )


@router.post("/refresh", response_model=RefreshResponse)
def refresh(payload: RefreshRequest, db: Session = Depends(get_db)) -> RefreshResponse:
    """Minta access token baru dengan refresh token yang masih berlaku."""
    try:
        data = decode_access_token(payload.refresh_token)
    except ValueError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Refresh token tidak valid")
    if data.get("typ") != "refresh":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token bukan refresh token")

    row = db.execute(select(RefreshToken).where(RefreshToken.token == payload.refresh_token)).scalar_one_or_none()
    if not row:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Refresh token tidak dikenal")
    if row.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        db.delete(row)
        db.commit()
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Refresh token kadaluarsa")

    # Rotasi: ganti refresh token lama dengan yang baru.
    db.delete(row)
    db.add(
        RefreshToken(
            user_id=str(row.user_id),
            token=create_refresh_token(str(row.user_id)),
            expires_at=datetime.now(timezone.utc) + timedelta(days=7),
        )
    )
    db.commit()

    return RefreshResponse(access_token=create_access_token(str(row.user_id)))


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(payload: RefreshRequest, db: Session = Depends(get_db)):
    """Hapus refresh token (sign-out)."""
    row = db.execute(select(RefreshToken).where(RefreshToken.token == payload.refresh_token)).scalar_one_or_none()
    if row:
        db.delete(row)
        db.commit()
