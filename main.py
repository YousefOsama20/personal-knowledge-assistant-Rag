from loaders import load_document
from chunker import chunk_documents


# --------------------------------
# 1. Load document
# --------------------------------

file_path = "data/uploads/test.txt"

documents = load_document(file_path)


print("=" * 60)
print("LOADED DOCUMENTS")
print("=" * 60)

print(f"Number of documents: {len(documents)}")


for document in documents:

    print("\n" + "-" * 60)

    print("SOURCE:")
    print(document["metadata"]["source"])

    print("PAGE:")
    print(document["metadata"]["page"])

    print("\nTEXT:")
    print(document["text"])


# --------------------------------
# 2. Chunk documents
# --------------------------------

chunks = chunk_documents(
    documents,
    chunk_size=200,
    overlap=50,
)


print("\n" + "=" * 60)
print("CHUNKS")
print("=" * 60)

print(f"Number of chunks: {len(chunks)}")


for i, chunk in enumerate(chunks, start=1):

    print("\n" + "-" * 60)
    print(f"CHUNK {i}")
    print("-" * 60)

    print("SOURCE:")
    print(chunk["metadata"]["source"])

    print("PAGE:")
    print(chunk["metadata"]["page"])

    print("\nTEXT:")
    print(chunk["text"])