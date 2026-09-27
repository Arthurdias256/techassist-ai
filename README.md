# \# TechAssist AI

# 

# API de Q\&A (perguntas e respostas) baseada em contexto, integrada com o

# Google Gemini. O usuário fornece um texto de referência (contexto) e faz

# perguntas sobre ele; a API responde apenas com base nesse contexto, evitando

# alucinações.

# 

# \## Categoria

# 

# Q\&A (Perguntas e Respostas) — disciplina IAW.

# 

# \## Tecnologias

# 

# \- Python 3.12

# \- FastAPI

# \- Google Generative AI SDK (Gemini)

# \- Slowapi (rate limiting)

# \- Pytest (testes)

# 

# \## Como rodar o projeto

# 

# \### 1. Clonar o repositório

# 

# \\`\\`\\`bash

# git clone <url-do-repositorio>.git

# cd techassist-ai

# \\`\\`\\`

# 

# \### 2. Criar e ativar o ambiente virtual

# 

# \\`\\`\\`bash

# python -m venv venv

# 

# \# Windows

# venv\\\\Scripts\\\\activate

# 

# \# Mac/Linux

# source venv/bin/activate

# \\`\\`\\`

# 

# \### 3. Instalar as dependências

# 

# \\`\\`\\`bash

# pip install -r requirements.txt

# \\`\\`\\`

# 

# \### 4. Configurar as variáveis de ambiente

# 

# Copie o arquivo de exemplo e preencha com sua chave real:

# 

# \\`\\`\\`bash

# cp .env.example .env

# \\`\\`\\`

# 

# Edite o `.env`:

# 

# \\`\\`\\`

# GEMINI\_API\_KEY=sua\_chave\_aqui

# \\`\\`\\`

# 

# Você pode gerar uma chave gratuita em

# \[Google AI Studio](https://aistudio.google.com/apikey).

# 

# \### 5. Rodar o servidor

# 

# \\`\\`\\`bash

# uvicorn main:app --reload

# \\`\\`\\`

# 

# A API estará disponível em `http://127.0.0.1:8000`.

# 

# \- Interface web: `http://127.0.0.1:8000/`

# \- Documentação Swagger: `http://127.0.0.1:8000/docs`

# 

# \### 6. Rodar os testes

# 

# \\`\\`\\`bash

# pytest -v

# \\`\\`\\`

# 

# \## Variáveis de ambiente

# 

# | Variável         | Descrição                          | Obrigatória |

# |------------------|-------------------------------------|-------------|

# | `GEMINI\_API\_KEY` | Chave de acesso à API do Gemini     | Sim         |

# 

# \## Rotas da API

# 

# \### `GET /health`

# 

# Verifica se a API está no ar.

# 

# \*\*Resposta (200):\*\*

# \\`\\`\\`json

# { "status": "ok" }

# \\`\\`\\`

# 

# \### `POST /perguntar`

# 

# Envia uma pergunta e um contexto para a IA responder.

# 

# \*\*Rate limit:\*\* 5 requisições por minuto por IP.

# 

# \*\*Corpo da requisição:\*\*

# \\`\\`\\`json

# {

# &#x20; "pergunta": "Qual a capital do Brasil?",

# &#x20; "contexto": "Brasília é a capital do Brasil desde 1960."

# }

# \\`\\`\\`

# 

# \*\*Restrições de validação:\*\*

# \- `pergunta`: 1 a 500 caracteres

# \- `contexto`: 1 a 5000 caracteres

# 

# \*\*Resposta de sucesso (200):\*\*

# \\`\\`\\`json

# { "resposta": "A capital do Brasil é Brasília." }

# \\`\\`\\`

# 

# \*\*Possíveis erros:\*\*

# 

# | Código | Situação                                         |

# |--------|---------------------------------------------------|

# | 422    | Pergunta ou contexto vazio, ausente ou muito longo |

# | 429    | Limite de requisições excedido                     |

# | 503    | Serviço de IA indisponível                         |

# | 504    | Tempo limite excedido ao consultar a IA            |

# | 500    | Erro inesperado no servidor                        |

# 

# \## Estrutura do projeto

# 

# \\`\\`\\`

# techassist-ai/

# ├── main.py              # Rotas da API e configuração do FastAPI

# ├── gemini\_service.py    # Integração com o Gemini (prompt, timeout, erros)

# ├── models.py            # Modelos Pydantic de request/response

# ├── test\_main.py         # Testes automatizados

# ├── static/

# │   └── index.html       # Interface web simples

# ├── requirements.txt

# ├── .env.example

# └── .gitignore

# \\`\\`\\`

