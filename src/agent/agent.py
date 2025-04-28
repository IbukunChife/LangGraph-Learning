from langgraph.graph import Graph
from graph_builder import build_graph

class Agente:
    """Encapsula o grafo compilado e expõe ask() para injeção de mensagens."""
    def __init__(self):
        # build_graph fornece CompiledGraph
        self.graph = build_graph()

    def ask(self, message: str):
        """
        Injeta `message` e executa o grafo via invoke().
        """
        # state inicial com user_input
        return self.graph.invoke({"user_input": message})