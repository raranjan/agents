import os
from functools import lru_cache


@lru_cache
def get_settings() -> dict:
    return {
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "app_name": os.getenv("APP_NAME", "research-agent"),
    }
