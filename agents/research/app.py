import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from shared.config import get_settings
# from shared.logging import setup_logging
from shared.models import HealthResponse, ResearchRequest, ResearchResponse
from agents.research.graph import run_research

logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup_logging()
    logger.info("Starting %s", settings.app_name)
    yield


app = FastAPI(
    title="Research Agent",
    description="Single-agent research service for the AgentStack platform.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service=settings.app_name)


@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest) -> ResearchResponse:
    try:
        result = run_research(request.query)
    except (FileNotFoundError, ValueError) as exc:
        logger.exception("Research workflow failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return ResearchResponse(
        query=result["query"],
        summary=result["summary"],
        status=result["status"],
    )
