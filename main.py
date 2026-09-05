from loaders import load_document


file_path = "data/uploads/test.txt"

text = load_document(file_path)

print("=" * 50)
print("EXTRACTED TEXT")
print("=" * 50)
print(text)