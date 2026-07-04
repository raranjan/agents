from agents.research.fake_llm import RESEARCH_SUMMARY


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "research-agent"


def test_research_returns_deterministic_json(client):
    response = client.post(
        "/research",
        json={"query": "Artificial Intelligence in Banking"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["query"] == "Artificial Intelligence in Banking"
    assert body["summary"] == RESEARCH_SUMMARY
    assert body["status"] == "success"


def test_research_rejects_empty_query(client):
    response = client.post("/research", json={"query": ""})
    assert response.status_code == 422
