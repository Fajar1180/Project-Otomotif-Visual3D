"""Database and application configuration."""
import os
from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment."""
    
    model_config = ConfigDict(env_file=".env", case_sensitive=False)

    # Database
    database_url: str = Field(
        default="sqlite:///:memory:",
        description="Database connection string (SQLite or PostgreSQL)"
    )
    
    # App
    debug: bool = Field(default=False, description="Debug mode")
    environment: str = Field(default="development", description="Environment name")
    openai_api_key: str = Field(default="", description="OpenAI API key")

    # Auth (override JWT_SECRET in production)
    jwt_secret: str = Field(default="dev-secret-change-me", description="HS256 signing key")
    jwt_expire_minutes: int = Field(default=60, description="Access token lifetime in minutes")

    # Celery / Redis (track A infra)
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis broker/backend URL")
    celery_task_always_eager: bool = Field(default=False, description="Run Celery tasks eagerly (tests/local without worker)")


settings = Settings()
