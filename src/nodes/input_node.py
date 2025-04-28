def InputNode(state):
    """Nó de entrada que coleta input do usuário."""
    # state vem vazio ou com contexto
    user_input = input("Pergunte algo: ")
    
    # Atualiza o estado com a entrada do usuário
    if state is None:
        state = {}
    
    state["user_input"] = user_input
    return state
