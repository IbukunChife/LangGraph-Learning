from langgraph.graph import Graph, START, END
from nodes.input_node import InputNode
from nodes.llm_node import LLMNode
from nodes.output_node import OutputNode

def build_graph() -> Graph:
    """Constrói e retorna um grafo compilado LangGraph."""
    g = Graph()
    # registra nós
    g.add_node("llm",    LLMNode)
    g.add_node("output", OutputNode)
    # define fluxo
    g.add_edge(START,    "llm")
    g.add_edge("llm",   "output")
    g.add_edge("output", END)
    # compile retorna CompiledGraph com método invoke()
    return g.compile()