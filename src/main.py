from loaders import load_document
from chunker import chunk_documents
from embeddings import EmbeddingModel
from vector_store import VectorStore
from llm import GeminiLLM
from rag import RAG

# ==========================================
# 1. Load document
# ==========================================

file_path = "data/uploads/test2.txt"

documents = load_document(file_path)

# ==========================================
# 2. Chunk document
# ==========================================

chunks = chunk_documents(
    documents,
    chunk_size=200,
    overlap=50,
)

# ==========================================
# 3. Create embeddings
# ==========================================

embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk["text"] for chunk in chunks]
)

# ==========================================
# 4. Store in vector database
# ==========================================

vector_store = VectorStore()

vector_store.add_documents(
    documents=[
        chunk["text"]
        for chunk in chunks
    ],
    embeddings=embeddings,
    ids=[
        f"test_chunk_{i}"
        for i in range(len(chunks))
    ],
    metadatas=[
        chunk["metadata"]
        for chunk in chunks
    ],
)

# ==========================================
# 5. Create LLM
# ==========================================

llm = GeminiLLM()


# ==========================================
# 6. Create RAG
# ==========================================

rag = RAG(
    embedding_model=embedding_model,
    vector_store=vector_store,
    llm=llm,
    top_k=3,
)

# ==========================================
# 7. Ask question
# ==========================================

result = rag.ask(
    "What is Retrieval Augmented Generation?"
)

# ==========================================
# 8. Print answer
# ==========================================

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(result["answer"])

# ==========================================
# 9. Print sources
# ==========================================

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for source in result["sources"]:
    print(
        source["metadata"]
    )