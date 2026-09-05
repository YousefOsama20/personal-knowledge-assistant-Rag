from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def embed_text(self, text: str) -> list[float]:
        """Convert one text into an embedding vector."""

        vector = self.model.encode(text)

        return vector.tolist()

    def embed_documents(self, documents: list[str] ) -> list[list[float]]:
        """Convert multiple documents into embedding vectors."""

        vectors = self.model.encode(documents)

        return vectors.tolist()