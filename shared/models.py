from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=1, examples=["Artificial Intelligence in Banking"])


class ResearchResponse(BaseModel):
    query: str
    summary: str
    status: str = "success"
