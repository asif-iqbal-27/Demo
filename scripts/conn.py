from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

# Qdrant Cloud Credentials
QDRANT_URL = "https://3dc63d2f-c7b0-4da5-96ee-a2428111e019.us-east4-0.gcp.cloud.qdrant.io"  # Replace with your Qdrant Cloud URL
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MzI5NTE4fQ.wfYypsDHHXiPXEybTd06BlDpK0bzIH6oGkTVNCVB0kE"  # Replace with your Qdrant Cloud API key

# Connect to Qdrant Cloud
client = QdrantClient(QDRANT_URL, api_key=API_KEY)

# Define Collection Name
COLLECTION_NAME = "chatbot_knowledge"

# Create Collection
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # 384 dimensions (same as embedding model)
)

print(f"Collection '{COLLECTION_NAME}' created successfully!")
