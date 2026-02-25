import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import FakeEmbeddings
from langchain_postgres.vectorstores import PGVector

# Configurações do Banco de Dados
CONNECTION_STRING = "postgresql+psycopg2://myuser:mypassword@localhost:5432/vectordb"
COLLECTION_NAME = "pdf_documents"

def ingest_pdf(file_path):
    print(f"Iniciando ingestão do arquivo: {file_path}")
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Documento dividido em {len(chunks)} chunks.")
    
    # Usando FakeEmbeddings com a dimensão padrão do OpenAI (1536)
    embeddings = FakeEmbeddings(size=1536)
    
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=CONNECTION_STRING,
        use_jsonb=True,
    )
    
    vector_store.add_documents(chunks)
    print("Ingestão concluída com sucesso (Simulada com FakeEmbeddings)!")

if __name__ == "__main__":
    pdf_path = "/home/ubuntu/document.pdf"
    if os.path.exists(pdf_path):
        ingest_pdf(pdf_path)
    else:
        print(f"Erro: Arquivo {pdf_path} não encontrado.")
