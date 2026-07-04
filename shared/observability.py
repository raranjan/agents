"""Langfuse observability integration."""

import logging

from langfuse import Langfuse

from shared.config import get_settings

logger = logging.getLogger(__name__)

_langfuse_client: Langfuse | None = None


def get_langfuse() -> Langfuse | None:
    """Get or initialize Langfuse client."""
    global _langfuse_client
    
    if _langfuse_client is not None:
        return _langfuse_client
    
    settings = get_settings()
    
    if not settings.langfuse_enabled:
        logger.info("Langfuse observability disabled")
        return None
    
    if not settings.langfuse_public_key or not settings.langfuse_secret_key:
        logger.warning("Langfuse enabled but credentials not provided, disabling")
        return None
    
    try:
        _langfuse_client = Langfuse(
            public_key=settings.langfuse_public_key,
            secret_key=settings.langfuse_secret_key,
            host=settings.langfuse_host,
        )
        logger.info("Langfuse observability initialized")
        return _langfuse_client
    except Exception as e:
        logger.error("Failed to initialize Langfuse: %s", e)
        return None
