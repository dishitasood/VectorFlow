import chromadb
import json
import ollama

with open("services/chunk_earnings_call.json", "r") as f:
    chunks = json.load(f)


client = chromadb.PersistentClient(path="./db")
existing = [c.name for c in client.list_collections()]
if "earnings_call" in existing:
    client.delete_collection(name="earnings_call")

collection = client.get_or_create_collection(name="earnings_call")

def embed_text(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]

assert len(embed_text("test")) == 768

documents = []
embeddings = []
metadatas = []
ids = []

for chunk in chunks:
    documents.append(chunk["text"])
    embeddings.append(embed_text(chunk["text"]))
    metadatas.append(chunk["metadata"])
    ids.append(str(chunk["chunk_id"]))

collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

# Quick Example
results = collection.query(
    query_texts=["What drove operating income growth in Q1 2024?"],
    n_results=3
)
