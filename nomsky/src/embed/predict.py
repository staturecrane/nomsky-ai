import uuid

import qdrant_client

from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

client = QdrantClient(url="http://qdrant:6333")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

try:
    client.create_collection(
        collection_name="document_collection",
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
except qdrant_client.http.exceptions.UnexpectedResponse:
    pass


def insert_vectors(topics: str, contents: str):
    embeddings = embedding_model.encode(topics)
    client.upsert(
        collection_name="document_collection",
        wait=True,
        points=[
            models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding.tolist(),
                payload={"topic": topic, "content": content},
            )
            for embedding, topic, content in zip(embeddings, topics, contents)
        ],
    )
