from langchain_openai import ChatOpenAI
from langchain_core.embeddings import FakeEmbeddings
from langchain_postgres.vectorstores import PGVector
from langchain_core.prompts import ChatPromptTemplate

CONNECTION_STRING = "postgresql+psycopg2://myuser:mypassword@localhost:5432/vectordb"
COLLECTION_NAME = "pdf_documents"

def test_query(pergunta):
    embeddings = FakeEmbeddings(size=1536)
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME,
        connection=CONNECTION_STRING,
    )
    
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
    
    prompt_template = ChatPromptTemplate.from_template("""
CONTEXTO: {contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

PERGUNTA DO USUÁRIO: {pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
""")

    docs_with_scores = vector_store.similarity_search_with_score(pergunta, k=10)
    contexto = "\n\n".join([doc.page_content for doc, score in docs_with_scores])
    
    chain = prompt_template | llm
    resposta = chain.invoke({
        "contexto": contexto,
        "pergunta": pergunta
    })
    
    print(f"PERGUNTA: {pergunta}")
    print(f"RESPOSTA: {resposta.content}\n")

if __name__ == "__main__":
    print("--- Iniciando Testes do Sistema ---\n")
    test_query("Qual o faturamento da Empresa SuperTechIABrazil?")
    test_query("Quantos clientes temos em 2024?")
    test_query("Qual a capital da França?")
