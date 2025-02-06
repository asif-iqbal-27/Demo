import json
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Qdrant Cloud Credentials
QDRANT_URL = "https://3dc63d2f-c7b0-4da5-96ee-a2428111e019.us-east4-0.gcp.cloud.qdrant.io"  # Replace with your Qdrant Cloud URL
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MzI5NTE4fQ.wfYypsDHHXiPXEybTd06BlDpK0bzIH6oGkTVNCVB0kE"  # Replace with your Qdrant Cloud API key

# Connect to Qdrant Cloud
client = QdrantClient(QDRANT_URL, api_key=API_KEY)

# Define Collection Name
COLLECTION_NAME = "chatbot_knowledge"

# Load Embeddings
with open("data/embedded_data.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Store Embeddings in Qdrant Cloud
points = [
    PointStruct(
        id=int(chunk["chunk_id"].replace("_", "")),  # Unique ID
        vector=chunk["embedding"],
        payload={"text": chunk["text"], "page": chunk["page"]}  # Metadata
    )
    for chunk in chunks
]

client.upsert(collection_name=COLLECTION_NAME, points=points)

print(f"Stored {len(points)} chunks in Qdrant Cloud.")
