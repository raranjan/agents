# AgentStack

Multi-agent platform bootstrap — a single research agent with shared SDK, LangGraph workflow, and Docker-based local development.

## Repository structure

```text
.
├── shared/                  # Shared SDK
│   ├── config.py
│   ├── logging.py
│   ├── models.py
│   └── sdk/              # LLM protocol, prompt helpers
├── agents/
│   └── research/             # Research agent (HTTP + graph)
├── infrastructure/
│   └── docker/               # Dockerfiles
├── docs/                     # Architecture, roadmap, ADRs
├── tests/                      # Unit and integration tests
├── collections/              # Bruno API collection
├── docker-compose.yml
├── Makefile
└── requirements.txt
```

Design principle: **transport (FastAPI) is separate from agent logic (LangGraph)**, and agents depend on the `LLMClient` protocol rather than a specific model vendor.

## Quick start

```bash
cp .env.example .env
make install
make test
make up
```

Or without Make:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
docker compose up --build
```

### Langfuse Observability

Langfuse runs locally via Docker Compose. Access the UI at [http://localhost:3000](http://localhost:3000).

API keys are configured in `.env.example` and enabled by default for Docker Compose. To disable Langfuse tracing, set `LANGFUSE_ENABLED=false` in `.env`.

Service URL: [http://localhost:8000](http://localhost:8000)

## API

| Method | Path        | Description              |
|--------|-------------|--------------------------|
| GET    | `/health`   | Liveness / health check  |
| POST   | `/research` | Run research workflow    |

### Examples

```bash
curl http://localhost:8000/health

curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"query": "Artificial Intelligence in Banking"}'
```

OpenAPI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Development

```bash
# Run tests
make test

# Run agent locally (no Docker)
export PYTHONPATH=shared:.
uvicorn agents.research.app:app --reload
```

## Documentation

- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [ADR 001: Repository structure](docs/adr/001-repository-structure.md)

## License

Private / unlicensed — update as needed.
