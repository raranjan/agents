# ADR 001: Repository structure

## Status

Accepted

## Context

We need a repository layout that supports a single research agent today and multiple agents, shared infrastructure, and observability later — without large refactors.

## Decision

Adopt the AgentStack layout:

```text
shared/            # Shared SDK
agents/            # One folder per agent service
infrastructure/    # Docker and future IaC
docs/              # Architecture, roadmap, ADRs
tests/             # Unit and integration tests
```

Additional conventions:

1. **Python package `shared`** provides config, logging, models, and SDK abstractions.
2. **`PYTHONPATH=shared:.`** so agents import `shared.*` and `agents.*`.
3. **HTTP stays thin** — `app.py` delegates to `graph.py`.
4. **LLM abstraction** — agents use `LLMClient` protocol; FakeLLM is swappable.

## Consequences

- Adding a new agent means a new folder under `agents/` plus an optional Dockerfile under `infrastructure/docker/`.
- Shared models and config change in one place (`shared/`).
- Docker build copies `shared/` and `agents/` with a fixed `PYTHONPATH`.

## Alternatives considered

- **`platform/` at repo root** — rejected; conflicts with Python stdlib `platform` module.
- **Monorepo with `src/shared`** — deferred; current layout keeps paths shallow.
