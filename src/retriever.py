from embeddings import EmbeddingModel
from vector_store import VectorStore


class Retriever:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        top_k: int = 3,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(
        self,
        question: str,
    ) -> list[dict]:
        """Retrieve the most relevant chunks."""

        # 1. Convert question to embedding
        question_embedding = (
            self.embedding_model.embed_text(question)
        )

        # 2. Search vector database
        results = self.vector_store.search(
            query_embedding=question_embedding,
            n_results=self.top_k,
        )

        # 3. Convert Chroma response
        retrieved_documents = []

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for document, metadata, distance in zip(documents, metadatas, distances):
            retrieved_documents.append(
                {
                    "text": document,
                    "metadata": metadata,
                    "distance": distance,
                }
            )

        return retrieved_documents
