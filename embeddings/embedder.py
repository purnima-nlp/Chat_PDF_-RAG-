import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def embed_texts(texts, model="text-embedding-3-small"):
    """
    Converts list of texts into embeddings.
    Returns numpy array.
    """
    response = client.embeddings.create(
        model=model,
        input=texts
    )

    vectors = [item.embedding for item in response.data]
    return np.array(vectors).astype("float32")


def embed_query(query, model="text-embedding-3-small"):
    return embed_texts([query], model=model)[0]

