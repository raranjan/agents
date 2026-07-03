# Research Swarm

Multi-agent platform foundation — Milestone 1 starts with a single FastAPI research agent.

## Project structure

```text
.
├── docker-compose.yml
├── gateway/              # API gateway (future)
├── agents/
│   └── research/         # Research agent service
├── shared/               # Shared models, config, logging
└── docs/
```

## Run locally (Docker Compose)

```bash
docker compose up --build
```

The service listens on [http://localhost:8000](http://localhost:8000).

## Run locally (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r agents/research/requirements.txt
export PYTHONPATH=.
uvicorn agents.research.app:app --reload
```

## Endpoints

| Method | Path     | Description        |
|--------|----------|--------------------|
| GET    | `/`      | Hello world        |
| GET    | `/health`| Health check       |

### Examples

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

OpenAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)
