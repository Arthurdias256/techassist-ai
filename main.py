from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from models import PerguntaRequest, PerguntaResponse
from gemini_service import (
    responder_pergunta,
    GeminiIndisponivelError,
    GeminiTimeoutError,
)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="TechAssist AI",
    description="API de Q&A baseada em contexto, integrada ao Gemini",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
def read_root():
    return {
        "message": "TechAssist AI API esta ativa.",
        "docs": "http://127.0.0.1:8000/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/perguntar", response_model=PerguntaResponse)
@limiter.limit("5/minute")
def perguntar(request: Request, dados: PerguntaRequest):
    try:
        resposta = responder_pergunta(dados.pergunta, dados.contexto)
    except GeminiTimeoutError:
        raise HTTPException(
            status_code=504,
            detail="A IA demorou demais para responder. Tente novamente.",
        )
    except GeminiIndisponivelError:
        raise HTTPException(
            status_code=503,
            detail="O servico de IA esta indisponivel no momento. Tente novamente em instantes.",
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Ocorreu um erro inesperado ao processar sua pergunta.",
        )
    return PerguntaResponse(resposta=resposta)

