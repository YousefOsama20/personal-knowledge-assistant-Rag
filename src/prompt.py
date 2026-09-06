
def build_prompt(
    question: str,
    retrieved_documents: list[dict],
) -> str:
    """Build a grounded prompt using retrieved documents."""

    context_parts = []

    for i, document in enumerate(
        retrieved_documents,
        start=1,
    ):
        text = document["text"]
        metadata = document["metadata"]

        source = metadata.get("source", "Unknown")
        page = metadata.get("page")

        if page:
            location = f"{source}, page {page}"
        else:
            location = source

        context_parts.append(
            f"[Source {i}: {location}]\n"
            f"{text}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I couldn't find the answer in the provided documents."

Do not invent information.

Always base your answer on the retrieved context.

Context:
--------------------
{context}
--------------------

Question:
{question}

Answer:
"""

    return prompt
