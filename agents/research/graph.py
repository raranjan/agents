from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, StateGraph

from agentstack.sdk.prompts import load_prompt, render_prompt
from agents.research.fake_llm import FakeLLM

PROMPT_PATH = Path(__file__).parent / "prompts" / "research_v1.md"


class ResearchState(TypedDict):
    query: str
    prompt: str
    summary: str
    status: str


def load_prompt_node(state: ResearchState) -> ResearchState:
    template = load_prompt(PROMPT_PATH)
    prompt = render_prompt(template, query=state["query"])
    return {**state, "prompt": prompt}


def invoke_llm_node(state: ResearchState, llm: FakeLLM | None = None) -> ResearchState:
    client = llm or FakeLLM()
    summary = client.invoke(state["prompt"])
    return {**state, "summary": summary}


def validate_output_node(state: ResearchState) -> ResearchState:
    summary = state["summary"].strip()
    if not summary:
        raise ValueError("LLM returned an empty summary")
    return {**state, "summary": summary, "status": "success"}


def build_research_graph(llm: FakeLLM | None = None):
    graph = StateGraph(ResearchState)
    graph.add_node("load_prompt", load_prompt_node)
    graph.add_node(
        "invoke_llm",
        lambda state: invoke_llm_node(state, llm=llm),
    )
    graph.add_node("validate_output", validate_output_node)
    graph.set_entry_point("load_prompt")
    graph.add_edge("load_prompt", "invoke_llm")
    graph.add_edge("invoke_llm", "validate_output")
    graph.add_edge("validate_output", END)
    return graph.compile()


def run_research(query: str, llm: FakeLLM | None = None) -> ResearchState:
    graph = build_research_graph(llm=llm)
    return graph.invoke({"query": query, "prompt": "", "summary": "", "status": "pending"})
