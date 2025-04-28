from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.agent import Agente
import uvicorn

app = FastAPI(title="LangGraph Learning API")

class Query(BaseModel):
    message: str

class Response(BaseModel):
    answer: str

# Inicializa o agente uma única vez
agent = Agente()

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do LangGraph Learning. Acesse /docs para a documentação."}

@app.post("/ask", response_model=Response)
async def ask(query: Query):
    try:
        result = agent.ask(query.message)
        return Response(answer=result.get("answer", "Sem resposta disponível"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)