"""Módulo de ingestão de documentos PDF para o sistema RAG."""
import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector

from config import (
    DATABASE_URL,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def ingest_pdf(file_path: str) -> bool:
    """Processa e armazena um PDF no banco vetorial.
    
    Args:
        file_path: Caminho para o arquivo PDF.
        
    Returns:
        True se a ingestão foi bem-sucedida, False caso contrário.
    """
    if not Path(file_path).exists():
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return False

    print(f"Iniciando ingestão do arquivo: {file_path}")
    
    # 1. Carregar o PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    # 2. Dividir em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Documento dividido em {len(chunks)} chunks.")
    
    # 3. Inicializar Embeddings
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    
    # 4. Armazenar no PostgreSQL com pgVector
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=DATABASE_URL,
        use_jsonb=True,
    )
    
    vector_store.add_documents(chunks)
    print("Ingestão concluída com sucesso!")
    return True


if __name__ == "__main__":
    PDF_PATH = "document.pdf"
    ingest_pdf(PDF_PATH)
