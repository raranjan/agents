import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    log_level: str = "INFO"
    app_name: str = "research-agent"
    host: str = "0.0.0.0"
    port: int = 8000


@lru_cache
def get_settings() -> Settings:
    return Settings(
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        app_name=os.getenv("APP_NAME", "research-agent"),
    )
