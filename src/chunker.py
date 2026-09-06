
def chunk_documents(
    documents: list[dict],
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[dict]:
    """
    Split documents into overlapping chunks
    while preserving metadata.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size"
        )

    chunks = []

    for document in documents:

        text = document["text"]
        metadata = document["metadata"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append(
                    {
                        "text": chunk_text,
                        "metadata": metadata.copy(),
                    }
                )

            start = end - overlap

    return chunks