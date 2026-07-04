from agents.research.fake_llm import GENERIC_RESPONSE, RESEARCH_SUMMARY, FakeLLM


def test_invoke_returns_research_summary_when_prompt_contains_research():
    llm = FakeLLM()
    assert llm.invoke("Please research this topic") == RESEARCH_SUMMARY


def test_invoke_returns_generic_response_otherwise():
    llm = FakeLLM()
    assert llm.invoke("What is the weather?") == GENERIC_RESPONSE
