import chromadb
import uuid


class VectorStore:
    def __init__(
        self,
        base_directory: str = "data/chroma",
    ):
        run_id = uuid.uuid4().hex

        persist_directory = (
            f"{base_directory}/run_{run_id}"
        )

        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="knowledge_base",
                configuration={
                    "hnsw": {
                        "space": "cosine"
                    }
                },
            )
        )

    def add_documents(
        self,
        documents: list[str],
        embeddings: list[list[float]],
        ids: list[str],
        metadatas: list[dict],
    ):
        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        
    def search(
        self,
        query_embedding: list[float],
        n_results: int = 3,
    ):
        """Search for the most similar documents."""

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )