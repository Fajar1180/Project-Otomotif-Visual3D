"""Database and application configuration.
Uses stdlib-only approach: os.getenv + fallback values.
No pydantic_settings dependency.
"""

from __future__ import annotations
import os
from typing import Final

# Build paths inside project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# === App settings ===
DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

# === Auth ===
JWT_SECRET: Final[str] = os.getenv("JWT_SECRET", "dev-secret-change-me")
JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

# === Database ===
DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "sqlite:///:memory:",
)

# === Redis / Celery ===
REDIS_URL: str = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0",
)

# === Shopee ===
SHOPEE_APP_ID: str = os.getenv("SHOPEE_APP_ID", "")
SHOPEE_APP_KEY: str = os.getenv("SHOPEE_APP_KEY", "")
SHOPEE_APP_SECRET: str = os.getenv("SHOPEE_APP_SECRET", "")


# Namespace so `from config import settings` works without pydantic_settings
class settings:  # ponytail: namespace class mirrors module-level vars; no pydantic_settings
    """Configuration namespace — stdlib-only, mirrors the module-level vars."""
    DEBUG = DEBUG
    ENVIRONMENT = ENVIRONMENT
    JWT_SECRET = JWT_SECRET
    JWT_EXPIRE_MINUTES = JWT_EXPIRE_MINUTES
    DATABASE_URL = DATABASE_URL
    database_url = DATABASE_URL
    redis_url = REDIS_URL
    SHOPEE_APP_ID = SHOPEE_APP_ID
    SHOPEE_APP_KEY = SHOPEE_APP_KEY
    SHOPEE_APP_SECRET = SHOPEE_APP_SECRET
    celery_task_always_eager = False
