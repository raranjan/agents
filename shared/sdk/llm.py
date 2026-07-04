from typing import Protocol, runtime_checkable


@runtime_checkable
class LLMClient(Protocol):
    """Contract for LLM backends. Agents depend on this, not a vendor SDK."""

    def invoke(self, prompt: str) -> str: ...
