def build_prompt(query, retrieved_chunks):
    context = "\n\n".join(
        f"Source: {c['source']}\n{c['text']}"
        for c in retrieved_chunks
    )

    prompt = f"""
You are a helpful assistant. Answer using only the provided context.

Context:
{context}

Question:
{query}

Answer clearly and concisely:
"""

    return prompt.strip()

