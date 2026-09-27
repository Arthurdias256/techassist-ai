from pydantic import BaseModel, Field

class PerguntaRequest(BaseModel):
    pergunta: str = Field(..., min_length=1, max_length=500, description="A pergunta a ser feita")
    contexto: str = Field(..., min_length=1, max_length=5000, description="O contexto no qual a resposta deve se basear")

class PerguntaResponse(BaseModel):
    resposta: str

