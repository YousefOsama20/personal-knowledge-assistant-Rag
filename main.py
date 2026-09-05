from loaders import load_document
from chunker import chunk_text


file_path = "data/uploads/test.txt"

# Step 1: Load document
text = load_document(file_path)

# Step 2: Split document into chunks
chunks = chunk_text(text, chunk_size=200, overlap=50)

print("=" * 60)
print("NUMBER OF CHUNKS")
print("=" * 60)

print(len(chunks))


for i, chunk in enumerate(chunks):
    print("\n" + "=" * 60)
    print(f"CHUNK {i + 1}")
    print("=" * 60)
    print(chunk)