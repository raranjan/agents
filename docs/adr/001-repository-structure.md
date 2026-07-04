# ADR 001: Repository structure

## Status

Accepted

## Context

We need a repository layout that supports a single research agent today and multiple agents, shared infrastructure, and observability later — without large refactors.

## Decision

Adopt the AgentStack layout:

```text
platform/          # Shared SDK (Python package: agentstack)
agents/            # One folder per agent service
infrastructure/    # Docker and future IaC
docs/              # Architecture, roadmap, ADRs
tests/             # Unit and integration tests
```

Additional conventions:

1. **Python package name `agentstack`** lives under `platform/` to avoid clashing with the stdlib `platform` module.
2. **`PYTHONPATH=platform:.`** so agents import `agentstack.*` and `agents.*`.
3. **HTTP stays thin** — `app.py` delegates to `graph.py`.
4. **LLM abstraction** — agents use `LLMClient` protocol; FakeLLM is swappable.

## Consequences

- Adding a new agent means a new folder under `agents/` plus an optional Dockerfile under `infrastructure/docker/`.
- Shared models and config change in one place (`platform/agentstack/`).
- Docker build copies `platform/` and `agents/` with a fixed `PYTHONPATH`.

## Alternatives considered

- **`shared/` at repo root** — rejected; bootstrap standardizes on `platform/`.
- **Monorepo with `src/agentstack`** — deferred; current layout matches milestone docs and keeps paths shallow.
