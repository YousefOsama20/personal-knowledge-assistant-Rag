from loaders import load_document
from chunker import chunk_documents
from embeddings import EmbeddingModel
from vector_store import VectorStore
from retriever import Retriever


# --------------------------------
# 1. Load document
# --------------------------------

file_path = "data/uploads/test2.txt"

documents = load_document(file_path)


# --------------------------------
# 2. Chunk documents
# --------------------------------

chunks = chunk_documents(
    documents,
    chunk_size=200,
    overlap=50,
)

# --------------------------------
# 3. Embeddings
# --------------------------------

embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    [chunk["text"] for chunk in chunks]
)

# --------------------------------
# 4. Metadata
# --------------------------------

metadatas = [chunk["metadata"] for chunk in chunks]

# --------------------------------
# 5. IDs
# --------------------------------

ids = [f"test_chunk_{i}" for i in range(len(chunks))]

# --------------------------------
# 6. Vector Store
# --------------------------------

vector_store = VectorStore()

vector_store.add_documents(
    documents=[
        chunk["text"]
        for chunk in chunks
    ],
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas,
)

# --------------------------------
# 7. Retriever
# --------------------------------

retriever = Retriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
    top_k=3,
)

# --------------------------------
# 8. Ask question
# --------------------------------

question = "What is Retrieval Augmented Generation?"

# --------------------------------
# 9. Retrieve
# --------------------------------

results = retriever.retrieve(question)

# --------------------------------
# 10. Display
# --------------------------------

print("\n" + "=" * 60)
print("QUESTION")
print("=" * 60)

print(question)


print("\n" + "=" * 60)
print("RETRIEVED CHUNKS")
print("=" * 60)


for i, result in enumerate(results, start=1):

    print("\n" + "-" * 60)
    print(f"RESULT {i}")
    print("-" * 60)

    print("TEXT:")
    print(result["text"])

    print("\nMETADATA:")
    print(result["metadata"])

    print("\nDISTANCE:")
    print(result["distance"])
