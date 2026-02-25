"""
Configurações centralizadas do sistema RAG.
Princípio Clean Code: DRY (Don't Repeat Yourself)
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Banco de Dados
DATABASE_URL: str = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/vectordb"
)
COLLECTION_NAME: str = "pdf_documents"

# Modelos OpenAI
EMBEDDING_MODEL: str = "text-embedding-3-small"
LLM_MODEL: str = "gpt-4o-mini"
LLM_TEMPERATURE: float = 0.0

# Configurações de Chunking
CHUNK_SIZE: int = 1000
CHUNK_OVERLAP: int = 150

# Configurações de Busca
SEARCH_K: int = 10

# Prompts
SYSTEM_PROMPT: str = """
CONTEXTO: {contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

PERGUNTA DO USUÁRIO: {pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

# Mensagens
MSG_NO_INFO: str = "Não tenho informações necessárias para responder sua pergunta."
MSG_EXIT_COMMANDS: tuple = ('sair', 'exit', 'quit')
