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


settings = Settings()
