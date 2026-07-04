from pathlib import Path


def load_prompt(path: Path | str) -> str:
    prompt_path = Path(path)
    if not prompt_path.is_file():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def render_prompt(template: str, **variables: str) -> str:
    rendered = template
    for key, value in variables.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered
