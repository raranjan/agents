from agents.research.fake_llm import RESEARCH_SUMMARY, FakeLLM
from agents.research.graph import run_research


def test_run_research_returns_deterministic_summary():
    result = run_research("Artificial Intelligence in Banking")
    assert result["query"] == "Artificial Intelligence in Banking"
    assert result["summary"] == RESEARCH_SUMMARY
    assert result["status"] == "success"


def test_run_research_accepts_injected_llm():
    class StubLLM(FakeLLM):
        def invoke(self, prompt: str) -> str:
            return "stub summary"

    result = run_research("test topic", llm=StubLLM())
    assert result["summary"] == "stub summary"
