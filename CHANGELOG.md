# Changelog

All notable changes to this project are documented here.

## [0.1.0] - 2026-07-04

### Added

- AgentStack repository structure (`shared/`, `agents/`, `infrastructure/`, `docs/`, `tests/`)
- Shared SDK (`shared`): config, logging, models, LLM protocol, prompt helpers
- Research agent with FastAPI, LangGraph workflow, and FakeLLM
- `GET /health` and `POST /research` endpoints
- Docker Compose and Dockerfile for local deployment
- Makefile, `.env.example`, Bruno API collection
- Unit and integration tests
- Architecture documentation, roadmap, and ADR 001
- Healthcheck in docker-compose.yml
- Type hints updated to accept LLMClient protocol for flexibility
- Test paths fixed to use relative path resolution
- Config simplified to use Pydantic Settings defaults
- Langfuse observability integration with optional tracing
- Observability module for Langfuse client initialization and tracing decorators
