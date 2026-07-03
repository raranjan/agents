from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str


class HelloResponse(BaseModel):
    message: str
    service: str = Field(default="research-agent")
