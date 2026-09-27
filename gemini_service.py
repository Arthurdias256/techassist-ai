import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY não configurada no .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """Você é um assistente de perguntas e respostas.
Responda SOMENTE com base no contexto fornecido abaixo.
Se a resposta não estiver no contexto, diga claramente que não sabe
e não invente informações.

Contexto:
{contexto}
"""

def responder_pergunta(pergunta: str, contexto: str) -> str:
    prompt = SYSTEM_PROMPT.format(contexto=contexto) + f"\n\nPergunta: {pergunta}"
    resposta = model.generate_content(prompt)
    return resposta.text