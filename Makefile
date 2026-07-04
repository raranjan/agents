.PHONY: help install test test-unit test-integration up down build logs clean

PYTHONPATH := platform:.
DOCKER_COMPOSE := docker compose

help:
	@echo "Targets: install, test, test-unit, test-integration, up, down, build, logs, clean"

install:
	pip install -r requirements.txt

test: test-unit test-integration

test-unit:
	PYTHONPATH=$(PYTHONPATH) pytest tests/unit -v

test-integration:
	PYTHONPATH=$(PYTHONPATH) pytest tests/integration -v

up:
	$(DOCKER_COMPOSE) up --build

down:
	$(DOCKER_COMPOSE) down

build:
	$(DOCKER_COMPOSE) build

logs:
	$(DOCKER_COMPOSE) logs -f research

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
