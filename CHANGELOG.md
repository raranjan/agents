# Changelog

All notable changes to this project are documented here.

## [0.1.0] - 2026-07-04

### Added

- AgentStack repository structure (`platform/`, `agents/`, `infrastructure/`, `docs/`, `tests/`)
- Platform SDK (`agentstack`): config, logging, models, LLM protocol, prompt helpers
- Research agent with FastAPI, LangGraph workflow, and FakeLLM
- `GET /health` and `POST /research` endpoints
- Docker Compose and Dockerfile for local deployment
- Makefile, `.env.example`, Bruno API collection
- Unit and integration tests
- Architecture documentation, roadmap, and ADR 001
