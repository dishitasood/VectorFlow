import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("cleaned_earnings_call.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["Fin"])

print("Embedding stored in Chroma")

