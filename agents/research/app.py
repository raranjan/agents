from contextlib import asynccontextmanager

from fastapi import FastAPI

from shared.config import get_settings
from shared.logging import setup_logging
from shared.models import HealthResponse, HelloResponse

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield


app = FastAPI(
    title="Research Agent",
    description="Hello-world FastAPI service for the research-swarm platform.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/", response_model=HelloResponse)
async def hello() -> HelloResponse:
    return HelloResponse(
        message="Hello from the research agent",
        service=settings["app_name"],
    )


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service=settings["app_name"])
