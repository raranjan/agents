# Architecture

AgentStack separates shared platform code from individual agent services so new agents can be added without duplicating infrastructure concerns.

## High-level architecture

```mermaid
flowchart TB
    Client[HTTP Client / Gateway]
    Research[Research Agent Service]
    Platform[AgentStack Platform SDK]
    Prompts[Prompt Files]
    FakeLLM[FakeLLM]

    Client -->|POST /research| Research
    Research --> Platform
    Research --> Prompts
    Research --> FakeLLM
    Platform -->|LLMClient protocol| FakeLLM
```

## Layering

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Transport | `agents/*/app.py` | HTTP routing, request/response models |
| Workflow | `agents/*/graph.py` | LangGraph state machine |
| LLM adapter | `agents/*/fake_llm.py` | Deterministic model stub (swap for real LLM later) |
| Platform SDK | `platform/agentstack/` | Config, logging, shared models, abstractions |

## Research agent sequence

```mermaid
sequenceDiagram
    participant C as Client
    participant API as FastAPI
    participant G as LangGraph
    participant P as Prompt loader
    participant L as FakeLLM

    C->>API: POST /research {query}
    API->>G: run_research(query)
    G->>P: load_prompt + render
    P-->>G: prompt string
    G->>L: invoke(prompt)
    L-->>G: summary
    G->>G: validate output
    G-->>API: ResearchState
    API-->>C: JSON response
```

## Scaling to multi-agent

Future agents follow the same pattern under `agents/<name>/`, reusing `platform/agentstack`. A gateway or supervisor (Milestone 3+) will route requests without changing individual agent internals.

See [ADR 001](adr/001-repository-structure.md) for structural decisions.
