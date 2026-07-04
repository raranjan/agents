# AgentStack

Multi-agent platform bootstrap — a single research agent with shared SDK, LangGraph workflow, and Docker-based local development.

## Repository structure

```text
.
├── platform/                 # Shared SDK (agentstack package)
│   └── agentstack/
│       ├── config.py
│       ├── logging.py
│       ├── models.py
│       └── sdk/              # LLM protocol, prompt helpers
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
export PYTHONPATH=platform:.
uvicorn agents.research.app:app --reload
```

## Documentation

- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [ADR 001: Repository structure](docs/adr/001-repository-structure.md)

## License

Private / unlicensed — update as needed.
