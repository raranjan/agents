from pathlib import Path

from shared.sdk.prompts import load_prompt, render_prompt


def test_load_prompt_reads_file():
    # Resolve path relative to test file location
    test_dir = Path(__file__).parent.parent.parent
    path = test_dir / "agents" / "research" / "prompts" / "research_v1.md"
    content = load_prompt(path)
    assert "research assistant" in content.lower()


def test_render_prompt_replaces_variables():
    template = "Query: {{query}}"
    rendered = render_prompt(template, query="AI in Banking")
    assert rendered == "Query: AI in Banking"
