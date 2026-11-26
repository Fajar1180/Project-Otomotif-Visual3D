"""Seed 2 dummy auth accounts (user + admin) via app/auth.hash_password."""
from __future__ import annotations

from app.auth import hash_password
from app.database import SessionLocal
from models import User

ACCOUNTS = [
    {"email": "user@otomotif.ai", "password": "UserOtomotif2026!", "full_name": "Budi Pengendara", "role": "user"},
    {"email": "admin@otomotif.ai", "password": "AdminOtomotif2026!", "full_name": "Admin Otomotif AI", "role": "admin"},
]


def seed_auth(db) -> None:
    """Create dummy accounts if they don't exist (idempotent)."""
    for acct in ACCOUNTS:
        existing = db.query(User).filter_by(email=acct["email"]).first()
        if existing:
            continue
        db.add(
            User(
                email=acct["email"],
                hashed_password=hash_password(acct["password"]),
                full_name=acct["full_name"],
                role=acct["role"],
            )
        )
    db.commit()


def main() -> None:
    db = SessionLocal()
    try:
        seed_auth(db)
        print("✓ Auth seed complete (user@otomotif.ai / admin@otomotif.ai)")
    finally:
        db.close()


if __name__ == "__main__":
    main()
