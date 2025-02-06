from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Qdrant Cloud Credentials
QDRANT_URL = "https://3dc63d2f-c7b0-4da5-96ee-a2428111e019.us-east4-0.gcp.cloud.qdrant.io"  # Replace with your Qdrant Cloud URL
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MzI5NTE4fQ.wfYypsDHHXiPXEybTd06BlDpK0bzIH6oGkTVNCVB0kE"  # Replace with your Qdrant Cloud API key

# Connect to Qdrant Cloud
client = QdrantClient(QDRANT_URL, api_key=API_KEY)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION_NAME = "chatbot_knowledge"

def search_query(query_text, top_k=3):
    query_embedding = model.encode(query_text).tolist()

    # Perform similarity search
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k
    )

    print("\nTop Matches:")
    for res in results:
        print(f"Score: {res.score:.4f} - Text: {res.payload['text'][:100]}...\n")

if __name__ == "__main__":
    search_query("Time Metrics")
