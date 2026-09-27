from fastapi import FastAPI
from gemini_service import responder_pergunta

app = FastAPI(
    title="TechAssist AI",
    description="API de Q&A baseada em contexto, integrada ao Gemini",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/perguntar")
def perguntar(pergunta: str, contexto: str):
    resposta = responder_pergunta(pergunta, contexto)
    return {"resposta": resposta}