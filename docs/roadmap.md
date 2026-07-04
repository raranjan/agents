# Roadmap

Platform evolution from a single agent to a full multi-agent stack.

## Milestone 1 — Bootstrap (current)

- [x] Repository structure (`platform/`, `agents/`, `infrastructure/`, `docs/`, `tests/`)
- [x] FastAPI research agent with `/health` and `/research`
- [x] LangGraph workflow with prompt loading
- [x] FakeLLM (deterministic, no external APIs)
- [x] Docker Compose local deployment
- [x] Unit and integration tests
- [x] Architecture docs, ADR, Bruno collection

## Milestone 2 — LangGraph enhancements

- Richer graph states and error handling
- Structured output validation

## Milestone 3 — Supervisor + multiple agents

- Orchestrator routing to specialized agents
- Shared request context

## Milestone 4 — Agent-to-agent (A2A) communication

- Internal agent messaging protocol

## Milestone 5 — Shared memory (Redis)

- Cross-agent session and memory store

## Milestone 6 — Prompt registry & versioning

- Centralized prompt management

## Milestone 7 — Langfuse observability

- Traces, spans, and evaluation hooks

## Milestone 8 — Evaluation service

- Automated quality checks on agent outputs

## Milestone 9 — Human-in-the-loop

- Approval gates and review workflows

## Milestone 10 — Production LLM

- Replace FakeLLM with Azure OpenAI / Foundry deployment
