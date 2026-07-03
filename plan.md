# Milestone 1 -- Single Agent (Hello Agent)

## Goal

Build the smallest possible agent-based application that establishes the
foundation for the entire platform.

By the end of this milestone you should have:

-   A single FastAPI service acting as an agent
-   A fake LLM that returns deterministic responses
-   A simple LangGraph workflow
-   Dockerized deployment
-   Local execution using Docker Compose
-   A clean project structure that will scale into a multi-agent
    platform

------------------------------------------------------------------------

# Learning Objectives

-   Understand the lifecycle of an agent
-   Separate transport (HTTP) from agent logic
-   Avoid coupling agent logic to a specific LLM
-   Establish reusable project conventions

------------------------------------------------------------------------

# Scope

Included:

-   FastAPI API
-   LangGraph workflow
-   FakeLLM implementation
-   Prompt loading from files
-   Dockerfile
-   docker-compose.yml
-   Basic logging
-   Health endpoint

Not included yet:

-   Multiple agents
-   A2A communication
-   Redis
-   Langfuse
-   Evaluation
-   Prompt versioning
-   Shared memory
-   Human approval

------------------------------------------------------------------------

# Suggested Project Structure

``` text
research-swarm/

├── docker-compose.yml
├── README.md
│
├── gateway/
│
├── agents/
│   └── research/
│       ├── app.py
│       ├── graph.py
│       ├── fake_llm.py
│       ├── prompts/
│       │   └── research_v1.md
│       ├── Dockerfile
│       └── requirements.txt
│
├── shared/
│   ├── models.py
│   ├── logging.py
│   └── config.py
│
└── docs/
```

------------------------------------------------------------------------

# Agent Flow

``` text
HTTP Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
LangGraph
      │
      ▼
Load Prompt
      │
      ▼
Fake LLM
      │
      ▼
Validate Output
      │
      ▼
Return JSON
```

------------------------------------------------------------------------

# Fake LLM

Implement a simple class with an `invoke(prompt: str)` method.

Expected behaviour:

-   If prompt contains "research"
    -   return a predefined summary
-   Otherwise
    -   return a generic response

No external APIs should be required.

------------------------------------------------------------------------

# Deliverables

-   [ ] Project skeleton created
-   [ ] Agent runs locally
-   [ ] Docker image builds
-   [ ] Docker Compose starts successfully
-   [ ] POST endpoint returns JSON
-   [ ] Prompt loaded from file
-   [ ] LangGraph executes successfully
-   [ ] Fake LLM integrated
-   [ ] README explains how to run

------------------------------------------------------------------------

# Acceptance Criteria

Running:

``` bash
docker compose up --build
```

should allow:

``` http
POST /research

{
  "query": "Artificial Intelligence in Banking"
}
```

and produce a deterministic JSON response.

------------------------------------------------------------------------

# Future Milestones

-   Milestone 2 --- LangGraph enhancements
-   Milestone 3 --- Supervisor + multiple agents
-   Milestone 4 --- A2A communication
-   Milestone 5 --- Shared memory (Redis)
-   Milestone 6 --- Prompt registry & versioning
-   Milestone 7 --- Langfuse observability
-   Milestone 8 --- Evaluation service
-   Milestone 9 --- Human-in-the-loop
-   Milestone 10 --- Replace FakeLLM with a real model
