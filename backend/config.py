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
JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))

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

# === 3D Engine Adapter (Issue #5) ===
THREE_D_ENGINE: str = os.getenv("THREE_D_ENGINE", "fallback")  # fallback | replicate | huggingface | external
REPLICATE_API_TOKEN: str = os.getenv("REPLICATE_API_TOKEN", "")
REPLICATE_MODEL_VERSION: str = os.getenv("REPLICATE_MODEL_VERSION", "")
HUGGINGFACE_API_TOKEN: str = os.getenv("HUGGINGFACE_API_TOKEN", "")
HUGGINGFACE_MODEL_ID: str = os.getenv("HUGGINGFACE_MODEL_ID", "")
EXTERNAL_3D_WORKER_URL: str = os.getenv("EXTERNAL_3D_WORKER_URL", "")
THREE_D_OUTPUT_DIR: str = os.getenv("THREE_D_OUTPUT_DIR", os.path.join(BASE_DIR, "generated_meshes"))


# === Fail fast: production must not boot on insecure defaults ===
# Learn more: an empty/known JWT secret lets anyone forge tokens; an empty
# DATABASE_URL silently falls back to SQLite in-memory and loses data on restart.
if ENVIRONMENT.lower() in ("production", "prod"):
    if not JWT_SECRET or JWT_SECRET in ("dev-secret-change-me", "change-me"):
        raise RuntimeError(
            "JWT_SECRET must be a strong, non-default value when ENVIRONMENT=production"
        )
    if not DATABASE_URL.startswith("postgresql"):
        raise RuntimeError(
            "DATABASE_URL must point to PostgreSQL when ENVIRONMENT=production"
        )


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
    THREE_D_ENGINE = THREE_D_ENGINE
    REPLICATE_API_TOKEN = REPLICATE_API_TOKEN
    REPLICATE_MODEL_VERSION = REPLICATE_MODEL_VERSION
    HUGGINGFACE_API_TOKEN = HUGGINGFACE_API_TOKEN
    HUGGINGFACE_MODEL_ID = HUGGINGFACE_MODEL_ID
    EXTERNAL_3D_WORKER_URL = EXTERNAL_3D_WORKER_URL
    THREE_D_OUTPUT_DIR = THREE_D_OUTPUT_DIR
