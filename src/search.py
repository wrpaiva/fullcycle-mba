"""Módulo de busca semântica no banco vetorial."""
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document

from config import (
    DATABASE_URL,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    SEARCH_K,
)


def get_vector_store() -> PGVector:
    """Retorna uma instância configurada do vector store."""
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    return PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )


def perform_search(query: str, k: int = SEARCH_K) -> list[tuple[Document, float]]:
    """Executa busca semântica no banco vetorial.
    
    Args:
        query: Texto da consulta.
        k: Número de resultados a retornar.
        
    Returns:
        Lista de tuplas (documento, score).
    """
    vector_store = get_vector_store()
    return vector_store.similarity_search_with_score(query, k=k)
