from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field, field_validator


# Find .env file relative to this settings.py file location
# This works regardless of where the app is run from
_settings_dir = Path(__file__).parent
_env_file = _settings_dir.parent / ".env"


class Settings(BaseSettings):
    # Database
    database_url: str = Field(
        default="sqlite:////app/artifact.db",
        env="DATABASE_URL"
    )
    
    # JWT Authentication
    # REQUIRED: Must be set via SECRET_KEY environment variable
    # Generate with: python -c "import secrets; print(secrets.token_hex(32))"
    secret_key: str = Field(
        env="SECRET_KEY",
        description="JWT secret key - MUST be set via environment variable"
    )
    
    algorithm: str = Field(
        default="HS256",
        env="ALGORITHM"
    )
    
    access_token_expire_minutes: int = Field(
        default=30,
        env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    
    # CORS - accepts comma-separated string or list, converts to list
    cors_origins: List[str] = Field(
        default=["http://localhost:5173"],
        env="CORS_ORIGINS"
    )
    
    # File Storage
    storage_root: str = Field(
        default="storage",
        env="STORAGE_BASE_PATH"
    )
    
    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            # Split by comma and strip whitespace
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        if isinstance(v, list):
            return v
        return ["http://localhost:5173"]
    
    @field_validator("secret_key")
    @classmethod
    def validate_secret_key(cls, v):
        # Prevent using placeholder, empty, or the old leaked key
        if not v:
            raise ValueError(
                "SECRET_KEY must be set via environment variable. "
                "Generate with: python -c 'import secrets; print(secrets.token_hex(32))'"
            )
        if v == "your-secret-key-here-change-in-production":
            raise ValueError(
                "SECRET_KEY cannot be the placeholder value. "
                "Generate with: python -c 'import secrets; print(secrets.token_hex(32))'"
            )
        # Block the old leaked key
        if v == "c292cf5033690f7b5727aba144768607e1bfd02da7d0810766a52959770cd914":
            raise ValueError(
                "SECRET_KEY cannot be the old hardcoded value. "
                "You MUST generate a new secret key via environment variable. "
                "Generate with: python -c 'import secrets; print(secrets.token_hex(32))'"
            )
        if len(v) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters long")
        return v
    
    model_config = SettingsConfigDict(
        env_file=_env_file,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


# Create a single instance
settings = Settings()

