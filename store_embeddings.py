from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(
    url="https://62a164fc-2caa-4062-8857-467e15dad1d3.us-east-1-1.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.m6Dt9VnA-c5jIOIw5NSzkisAViySdjdhRUvmkUxebGE"
)


client.recreate_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

client.upsert(
    collection_name="documents",
    points=[
        {"id": 1, "vector": [0.1]*384, "payload": {"text": "Hello"}},
        {"id": 2, "vector": [0.2]*384, "payload": {"text": "World"}}
    ]
)

res = client.search(

    collection_name="documents",
    query_vector=[0.1]*384,
    limit=2
)

print(res)
