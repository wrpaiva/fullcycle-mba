# Ingestão e Busca Semântica com LangChain e Postgres (pgVector)

Este projeto implementa um sistema de RAG (Retrieval-Augmented Generation) que processa arquivos PDF e permite consultas via CLI utilizando PostgreSQL com a extensão pgVector.

## Estrutura do Projeto

```text
├── docker-compose.yml 
├── requirements.txt      # Dependências 
├── .env.example          # Template da variável OPENAI_API_KEY 
├── src/ 
│   ├── ingest.py         # Script de ingestão do PDF 
│   ├── search.py         # Script de busca 
│   └── chat.py           # CLI para interação com usuário 
├── document.pdf          # PDF para ingestão 
└── README.md             # Instruções de execução
```

## Tecnologias Obrigatórias

- **Linguagem:** Python
- **Framework:** LangChain
- **Banco de Dados:** PostgreSQL + pgVector
- **Embeddings:** `text-embedding-3-small`
- **LLM:** `gpt-5-nano` (ou `gpt-4o-mini`)

## Ordem de Execução

### 1. Subir o banco de dados
```bash
docker compose up -d
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar ingestão do PDF
Certifique-se de que o arquivo `document.pdf` está na raiz do projeto.
```bash
python src/ingest.py
```

### 4. Rodar o chat
```bash
python src/chat.py
```

## Regras de Resposta
O sistema responde apenas com base no conteúdo do PDF. Caso a informação não esteja presente, a resposta padrão será: *"Não tenho informações necessárias para responder sua pergunta."*
