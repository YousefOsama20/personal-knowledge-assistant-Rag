from embeddings import EmbeddingModel
from vector_store import VectorStore
from retriever import Retriever
from llm import GeminiLLM
from prompt import build_prompt


class RAG:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        llm: GeminiLLM,
        top_k: int = 3,
    ):
        self.embedding_model = embedding_model

        self.vector_store = vector_store

        self.retriever = Retriever(
            embedding_model=embedding_model,
            vector_store=vector_store,
            top_k=top_k,
        )

        self.llm = llm

    def ask(self,question: str) -> dict:
        """Answer a question using RAG."""

        # 1. Retrieve relevant documents
        retrieved_documents = (
            self.retriever.retrieve(question)
        )

        # 2. Build grounded prompt
        prompt = build_prompt(
            question=question,
            retrieved_documents=retrieved_documents,
        )

        # 3. Generate answer
        answer = self.llm.generate(prompt)

        # 4. Return answer and sources
        return {
            "answer": answer,
            "sources": retrieved_documents,
        }