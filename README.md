# 🤖 RAG System - Busca Semântica com LangChain e pgVector

Sistema de **Retrieval-Augmented Generation (RAG)** que processa documentos PDF e permite consultas em linguagem natural via CLI, utilizando PostgreSQL com pgVector para armazenamento de embeddings.

## 📋 Sobre o Projeto

Este projeto implementa um chatbot inteligente que responde perguntas **exclusivamente** com base no conteúdo de documentos PDF ingeridos. Utiliza busca semântica vetorial para encontrar contexto relevante e um modelo de linguagem (LLM) para gerar respostas precisas.

### Características Principais

- ✅ **Ingestão de PDFs** com chunking otimizado (1000 caracteres, 150 overlap)
- ✅ **Busca semântica** via embeddings vetoriais
- ✅ **Respostas contextualizadas** - não inventa informações
- ✅ **Interface CLI** simples e intuitiva
- ✅ **Banco vetorial** PostgreSQL + pgVector via Docker
- ✅ **Clean Code** - código modular, tipado e sem duplicação

## 🛠️ Tecnologias

| Componente | Tecnologia |
|------------|------------|
| Linguagem | Python 3.x |
| Framework | LangChain |
| Banco de Dados | PostgreSQL 16 + pgVector |
| Embeddings | `text-embedding-3-small` (OpenAI) |
| LLM | `gpt-4o-mini` (OpenAI) |
| Container | Docker / Docker Compose |

## 📁 Estrutura do Projeto

```
├── docker-compose.yml      # Configuração do PostgreSQL + pgVector
├── requirements.txt        # Dependências Python
├── document.pdf            # PDF para ingestão (adicionar manualmente)
├── src/
│   ├── config.py           # 🎯 Configurações centralizadas (Clean Code)
│   ├── ingest.py           # Script de ingestão do PDF
│   ├── search.py           # Módulo de busca semântica
│   └── chat.py             # CLI principal para interação
├── tests/
│   ├── __init__.py         # Módulo de testes
│   ├── test_models.py      # Testes de modelos OpenAI
│   ├── test_system.py      # Testes do sistema RAG
│   └── ingestion_fake.py   # Ingestão com FakeEmbeddings
├── generate_pdf.py         # Utilitário para gerar PDF de exemplo
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.8+ 
- Chave de API da OpenAI

### 1. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
OPENAI_API_KEY=sua_chave_api_aqui
DATABASE_URL=postgresql+psycopg2://myuser:mypassword@localhost:5432/vectordb
```

### 2. Subir o banco de dados

```bash
docker compose up -d
```

O container irá inicializar o PostgreSQL com a extensão pgVector na porta `5432`.

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Adicionar o documento PDF

Coloque seu arquivo PDF na raiz do projeto com o nome `document.pdf`.

### 5. Executar a ingestão

```bash
python src/ingest.py
```

Isso irá:
- Carregar o PDF
- Dividir em chunks de 1000 caracteres
- Gerar embeddings com `text-embedding-3-small`
- Armazenar no PostgreSQL/pgVector

### 6. Iniciar o chat

```bash
python src/chat.py
```

## 💬 Usando o Chat

```
--- Chat CLI SuperTechIABrazil ---
Digite sua pergunta ou 'sair' para encerrar.

Faça sua pergunta: Qual o faturamento da empresa?
RESPOSTA: O faturamento da Empresa SuperTechIABrazil no último período foi de 10 milhões de reais.

Faça sua pergunta: Qual a capital da França?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.

Faça sua pergunta: sair
```

## 📐 Arquitetura

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   PDF       │────▶│   Ingestão   │────▶│  PostgreSQL     │
│   Input     │     │  (chunks +   │     │  + pgVector     │
│             │     │   embeddings)│     │  (vetores)      │
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                  │
┌─────────────┐     ┌──────────────┐              │
│   Usuário   │────▶│   Chat CLI   │◀─────────────┘
│  (pergunta) │     │              │     Busca Semântica
└─────────────┘     └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   OpenAI     │
                    │   GPT-4o     │
                    │   (resposta) │
                    └──────────────┘
```

## ⚙️ Configurações Técnicas

| Parâmetro | Valor |
|-----------|-------|
| Chunk Size | 1000 caracteres |
| Chunk Overlap | 150 caracteres |
| Busca (k) | 10 documentos mais relevantes |
| Temperature LLM | 0 (respostas determinísticas) |
| Dimensão Embeddings | 1536 |

## 🧪 Testes

### Testar modelos OpenAI disponíveis
```bash
python tests/test_models.py
```

### Testar sistema com queries de exemplo
```bash
python tests/test_system.py
```

### Ingestão com FakeEmbeddings (sem API)
```bash
python tests/ingestion_fake.py
```

## 🧼 Clean Code

Este projeto segue os princípios de **Clean Code**:

| Princípio | Implementação |
|-----------|---------------|
| **DRY** (Don't Repeat Yourself) | Configurações centralizadas em `config.py` |
| **Single Responsibility** | Cada módulo tem uma única responsabilidade |
| **Type Hints** | Funções tipadas com anotações Python |
| **Docstrings** | Documentação clara em todas as funções |
| **Constantes Nomeadas** | Valores mágicos substituídos por constantes |
| **Funções Pequenas** | Funções focadas e fáceis de testar |

### Exemplo de Configuração Centralizada

```python
# src/config.py
from config import (
    DATABASE_URL,       # Conexão com banco
    COLLECTION_NAME,    # Nome da coleção vetorial
    EMBEDDING_MODEL,    # Modelo de embeddings
    LLM_MODEL,          # Modelo de linguagem
    CHUNK_SIZE,         # Tamanho dos chunks
    SEARCH_K,           # Número de resultados
)
```

## 📝 Regras de Resposta

O sistema segue regras estritas:

1. **Responde APENAS** com base no conteúdo do PDF ingerido
2. **Não inventa** informações ou usa conhecimento externo
3. **Não emite opiniões** ou interpretações além do texto
4. Quando a informação não está disponível, responde:
   > "Não tenho informações necessárias para responder sua pergunta."

## 🐳 Docker

### Verificar status do container
```bash
docker compose ps
```

### Ver logs do PostgreSQL
```bash
docker compose logs db
```

### Parar o ambiente
```bash
docker compose down
```

### Resetar o banco de dados
```bash
docker compose down -v
docker compose up -d
```

## 📚 Dependências

```
langchain
langchain-openai
langchain-postgres
langchain-community
pypdf
psycopg2-binary
tiktoken
python-dotenv
```

## 🎓 Contexto

Projeto desenvolvido para o **MBA Full Cycle** como estudo de implementação de sistemas RAG com busca semântica vetorial.

---

**Feito com ❤️ usando LangChain + pgVector**
