import pytest
from fastapi.testclient import TestClient

from agents.research.app import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
