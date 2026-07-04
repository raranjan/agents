RESEARCH_SUMMARY = (
    "Research summary: The topic involves structured analysis of the subject matter, "
    "covering key trends, stakeholders, and practical implications."
)

GENERIC_RESPONSE = "I can help with research queries. Please provide a specific topic to analyze."


class FakeLLM:
    """Deterministic LLM stub for local development and tests."""

    def invoke(self, prompt: str) -> str:
        if "research" in prompt.lower():
            return RESEARCH_SUMMARY
        return GENERIC_RESPONSE
