import json
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # You can replace with another model

# Load processed text chunks
with open("data/processed_data.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Convert text chunks into embeddings
for chunk in chunks:
    chunk["embedding"] = model.encode(chunk["text"]).tolist()  # Convert to list

# Save embeddings
with open("data/embedded_data.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)

print(f"Generated embeddings for {len(chunks)} chunks.")
