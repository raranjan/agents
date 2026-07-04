# AgentStack - Project Master Plan

## Vision

Build an enterprise-grade, modular, observable, and extensible multi-agent platform that demonstrates how modern AI agents collaborate to solve complex tasks.

The platform begins as a Research Swarm and evolves into a CRM automation platform supporting intelligent routing, enrichment, autonomous execution, and human-in-the-loop workflows.

## Project Goals

- Multi-agent collaboration
- A2A communication
- LangGraph orchestration
- Prompt management & versioning
- Shared memory
- Observability
- Evaluation
- Human approval
- MCP integration
- Real LLM support
- Enterprise deployment

## Guiding Principles

- Platform First
- SDK First
- Contract First
- Observable by Default
- Provider Agnostic

## Repository Structure

```text
agentstack/
├── docker-compose.yml
├── pyproject.toml
├── README.md
├── Makefile
├── .env.example
├── .gitignore
├── docs/
├── platform/
├── agents/
├── infrastructure/
└── tests/
```

## Technology Stack

- Python 3.12
- uv
- FastAPI
- LangGraph
- Pydantic v2
- Ruff
- Pytest
- Docker
- Docker Compose
- Redis (later)
- Langfuse (later)
- A2A
- MCP
- FakeLLM → Ollama/OpenAI/Bedrock

## Milestone Roadmap

1. Platform Bootstrap
2. Agent SDK
3. LangGraph Runtime
4. Supervisor
5. A2A Communication
6. Memory
7. Prompt Platform
8. Observability
9. Evaluation
10. Enterprise Runtime

## Deliverables Per Milestone

- Updated README
- Updated Architecture
- Updated Sequence Diagrams
- Updated ADRs
- Updated Roadmap
- Makefile
- Docker Compose
- .env.example
- .gitignore
- API Collection
- Unit Tests
- Integration Tests
- Validation Checklist
- Release Notes

## Definition of Done

- Tests pass
- Docker Compose builds
- Documentation updated
- Diagrams updated
- ADRs updated
- Runs from clean clone
- Ready for Git tag

## Cursor Development Instructions

- Use type hints everywhere.
- Keep business logic out of FastAPI handlers.
- Store prompts as Markdown.
- Use Pydantic models.
- Update docs, diagrams, ADRs and tests with every feature.
- Avoid unnecessary dependencies.

## Long-Term Vision

AgentStack becomes a reusable enterprise AI platform for CRM, document intelligence, research, and financial assistant use cases.
