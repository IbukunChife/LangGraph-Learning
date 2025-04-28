from agent.agent import Agente

def main():
    agent = Agente()
    print("=== Agente LangGraph Iniciado ===")
    while True:
        msg = input("Você: ").strip()
        if msg.lower() in ("sair", "exit", "quit"):
            print("Encerrando... Até mais! 👋")
            break
        # chama apenas ask() — sem input_node extra
        agent.ask(msg)


if __name__ == "__main__":
    main()
