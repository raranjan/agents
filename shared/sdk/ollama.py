from __future__ import annotations

import requests

from shared.sdk.llm import LLMClient


class OllamaLLM(LLMClient):
    """LLM client backed by a locally running Ollama server."""

    def __init__(
        self,
        model: str = "gemma4:latest",
        base_url: str = "http://host.docker.internal:11434",
        timeout: int = 120,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def invoke(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=self.timeout,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"].strip()