from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, StateGraph

from shared.observability import get_langfuse
from shared.sdk.llm import LLMClient
from shared.sdk.prompts import load_prompt, render_prompt
from agents.research.fake_llm import FakeLLM
from shared.sdk.ollama import OllamaLLM

PROMPT_PATH = Path(__file__).parent / "prompts" / "research_v1.md"


class ResearchState(TypedDict):
    query: str
    prompt: str
    summary: str
    status: str


def load_prompt_node(state: ResearchState) -> ResearchState:
    langfuse = get_langfuse()
    if langfuse:
        langfuse.create_event(name="load_prompt", input=state)
    
    template = load_prompt(PROMPT_PATH)
    prompt = render_prompt(template, query=state["query"])
    result = {**state, "prompt": prompt}
    
    if langfuse:
        langfuse.create_event(name="load_prompt", output=result)
    
    return result


def invoke_llm_node(state: ResearchState, llm: LLMClient | None = None) -> ResearchState:
    langfuse = get_langfuse()
    if langfuse:
        langfuse.create_event(name="invoke_llm", input=state)
    
    client = llm or OllamaLLM()
    summary = client.invoke(state["prompt"])
    result = {**state, "summary": summary}
    
    if langfuse:
        langfuse.create_event(name="invoke_llm", output=result)
    
    return result


def validate_output_node(state: ResearchState) -> ResearchState:
    summary = state["summary"].strip()
    if not summary:
        raise ValueError("LLM returned an empty summary")
    return {**state, "summary": summary, "status": "success"}


def build_research_graph(llm: LLMClient | None = None):
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


def run_research(query: str, llm: LLMClient | None = None) -> ResearchState:
    langfuse = get_langfuse()
    if langfuse:
        langfuse.create_event(name="research_workflow", input={"query": query})
    
    graph = build_research_graph(llm=llm)
    result = graph.invoke({"query": query, "prompt": "", "summary": "", "status": "pending"})
    
    if langfuse:
        langfuse.create_event(name="research_workflow", output=result)
        langfuse.flush()
    
    return result
