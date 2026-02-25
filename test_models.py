from openai import OpenAI
client = OpenAI()

try:
    print("Testando gpt-4.1-mini para embeddings...")
    response = client.embeddings.create(
        input="Teste de embedding",
        model="gpt-4.1-mini"
    )
    print("Sucesso com gpt-4.1-mini")
except Exception as e:
    print(f"Erro com gpt-4.1-mini: {e}")

try:
    print("\nTestando text-embedding-3-small no endpoint customizado...")
    response = client.embeddings.create(
        input="Teste de embedding",
        model="text-embedding-3-small"
    )
    print("Sucesso com text-embedding-3-small")
except Exception as e:
    print(f"Erro com text-embedding-3-small: {e}")

try:
    print("\nListando modelos disponíveis...")
    models = client.models.list()
    for model in models:
        print(f"- {model.id}")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")
