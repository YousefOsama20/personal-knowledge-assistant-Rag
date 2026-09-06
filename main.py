from loaders import load_document
from chunker import chunk_text
from embeddings import EmbeddingModel
from vector_store import VectorStore

# --------------------------------
# 1. Load document
# --------------------------------

file_path = "data/uploads/test.txt"

text = load_document(file_path)


# --------------------------------
# 2. Chunk document
# --------------------------------

chunks = chunk_text(
    text,
    chunk_size=200,
    overlap=50,
)

# --------------------------------
# 3. Create embeddings
# --------------------------------

embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_documents(
    chunks
)

# --------------------------------
# 4. Create metadata
# --------------------------------

metadatas = []

for i in range(len(chunks)):
    metadatas.append({
        "source": "test.txt",
        "chunk": i + 1,
    })


# --------------------------------
# 5. Create IDs
# --------------------------------

ids = [
    f"test_txt_chunk_{i + 1}"
    for i in range(len(chunks))
]

# --------------------------------
# 6. Create vector store
# --------------------------------

vector_store = VectorStore()

# --------------------------------
# 7. Store everything
# --------------------------------

vector_store.add_documents(
    documents=chunks,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas,
)


print("=" * 60)
print("DOCUMENT STORED SUCCESSFULLY")
print("=" * 60)

print(f"Number of chunks: {len(chunks)}")

# --------------------------------
# 8. Ask a question
# --------------------------------

question = "What is Retrieval Augmented Generation?"


# --------------------------------
# 9. Embed the question
# --------------------------------

question_embedding = embedding_model.embed_text(
    question
)


# --------------------------------
# 10. Search Chroma
# --------------------------------

results = vector_store.search(
    query_embedding=question_embedding,
    n_results=3,
)


# --------------------------------
# 11. Display results
# --------------------------------

print("\n" + "=" * 60)
print("SEARCH RESULTS")
print("=" * 60)


for i, document in enumerate(
    results["documents"][0]
):

    print("\n" + "-" * 60)
    print(f"RESULT {i + 1}")
    print("-" * 60)

    print(document)
