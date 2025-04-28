import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

def LLMNode(state, prompt_template="Responda de forma clara: {input}"):
    """Nó que processa a entrada do usuário usando um modelo de linguagem."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    text = state.get("user_input", "")
    prompt = prompt_template.format(input=text)
    
    resp = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[{"role": "user", "content": prompt}]
    )
    
    answer = resp.choices[0].message.content
    state["answer"] = answer
    
    return state
