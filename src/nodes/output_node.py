def OutputNode(state):
    """Nó de saída que exibe a resposta do LLM."""
    print("🤖", state.get("answer", "Sem resposta disponível"))
    return state