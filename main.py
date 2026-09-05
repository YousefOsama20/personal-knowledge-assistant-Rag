from loaders import load_document
from chunker import chunk_text
from embeddings import EmbeddingModel

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
# 3. Create embedding model
# --------------------------------

embedding_model = EmbeddingModel()

# --------------------------------
# 4. Create embeddings
# --------------------------------

vectors = embedding_model.embed_documents(chunks)

# --------------------------------source .venv/bin/activate

# 5. Display results
# --------------------------------

print("=" * 60)
print("NUMBER OF CHUNKS")
print("=" * 60)

print(len(chunks))


for i, (chunk, vector) in enumerate(
    zip(chunks, vectors)
):

    print("\n" + "=" * 60)
    print(f"CHUNK {i + 1}")
    print("=" * 60)

    print(chunk)

    print("\nVECTOR:")
    print(vector[:10])

    print("\nVECTOR DIMENSION:")
    print(len(vector))