"""Interface CLI para interação com o sistema RAG."""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config import (
    LLM_MODEL,
    LLM_TEMPERATURE,
    SYSTEM_PROMPT,
    SEARCH_K,
    MSG_EXIT_COMMANDS,
)
from search import perform_search


def build_context(docs_with_scores: list) -> str:
    """Concatena o conteúdo dos documentos encontrados."""
    return "\n\n".join([doc.page_content for doc, _ in docs_with_scores])


def main() -> None:
    """Loop principal do chat CLI."""
    llm = ChatOpenAI(model=LLM_MODEL, temperature=LLM_TEMPERATURE)
    prompt_template = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
    
    print("--- Chat CLI SuperTechIABrazil ---")
    print("Digite sua pergunta ou 'sair' para encerrar.")

    while True:
        try:
            pergunta = input("\nFaça sua pergunta: ")
            
            if pergunta.lower() in MSG_EXIT_COMMANDS:
                print("Encerrando chat...")
                break
            
            # Buscar documentos relevantes
            docs_with_scores = perform_search(pergunta, k=SEARCH_K)
            contexto = build_context(docs_with_scores)
            
            # Gerar resposta com LLM
            chain = prompt_template | llm
            resposta = chain.invoke({
                "contexto": contexto,
                "pergunta": pergunta,
            })
            
            print(f"RESPOSTA: {resposta.content}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando chat...")
            break
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
