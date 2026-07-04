from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    log_level: str = "INFO"
    app_name: str = "research-agent"
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Langfuse configuration
    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str = "https://cloud.langfuse.com"
    langfuse_enabled: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
