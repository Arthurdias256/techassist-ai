import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY nao configurada no .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

SYSTEM_PROMPT = """Voce e um assistente de perguntas e respostas.
Responda SOMENTE com base no contexto fornecido abaixo.
Se a resposta nao estiver no contexto, diga claramente que nao sabe e nao invente informacoes.

Contexto:
{contexto}"""

class GeminiIndisponivelError(Exception):
    pass

def responder_pergunta(pergunta: str, contexto: str) -> str:
    prompt = SYSTEM_PROMPT.format(contexto=contexto) + f"\n\nPergunta: {pergunta}"
    try:
        resposta = model.generate_content(prompt)
    except Exception as e:
        raise GeminiIndisponivelError(str(e))
    
    if not resposta.text:
        raise GeminiIndisponivelError("Resposta vazia da IA")
        
    return resposta.text.strip()

