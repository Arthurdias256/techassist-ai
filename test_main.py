from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_perguntar_sucesso():
    with patch("main.responder_pergunta", return_value="Resposta simulada da IA"):
        response = client.post(
            "/perguntar",
            json={"pergunta": "Qual a capital do Brasil?", "contexto": "Brasilia e a capital do Brasil."},
        )
    assert response.status_code == 200
    assert response.json() == {"resposta": "Resposta simulada da IA"}

def test_perguntar_pergunta_vazia():
    response = client.post(
        "/perguntar",
        json={"pergunta": "", "contexto": "Algum contexto valido."},
    )
    assert response.status_code == 422

def test_perguntar_contexto_vazio():
    response = client.post(
        "/perguntar",
        json={"pergunta": "Alguma pergunta?", "contexto": ""},
    )
    assert response.status_code == 422

def test_perguntar_campos_faltando():
    response = client.post("/perguntar", json={})
    assert response.status_code == 422

def test_perguntar_gemini_timeout():
    from gemini_service import GeminiTimeoutError
    with patch("main.responder_pergunta", side_effect=GeminiTimeoutError()):
        response = client.post(
            "/perguntar",
            json={"pergunta": "Pergunta qualquer", "contexto": "Contexto qualquer"},
        )
    assert response.status_code == 504

def test_perguntar_gemini_indisponivel():
    from gemini_service import GeminiIndisponivelError
    with patch("main.responder_pergunta", side_effect=GeminiIndisponivelError()):
        response = client.post(
            "/perguntar",
            json={"pergunta": "Pergunta qualquer", "contexto": "Contexto qualquer"},
        )
    assert response.status_code == 503

