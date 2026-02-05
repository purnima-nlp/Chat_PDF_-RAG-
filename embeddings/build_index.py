import json
import os
import pickle
import faiss
import numpy as np
from embeddings.embedder import embed_texts


CHUNKS_PATH = "data/chunks/chunks.json"
INDEX_PATH = "vector.index"
META_PATH = "metadata.pkl"


def load_chunks():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index


def save_index(index):
    faiss.write_index(index, INDEX_PATH)


def save_metadata(chunks):
    with open(META_PATH, "wb") as f:
        pickle.dump(chunks, f)


def main():
    chunks = load_chunks()
    texts = [c["text"] for c in chunks]

    print("Embedding chunks...")
    vectors = embed_texts(texts)

    print("Building FAISS index...")
    index = build_faiss_index(vectors)

    save_index(index)
    save_metadata(chunks)

    print(f"Saved {len(texts)} vectors to FAISS")


if __name__ == "__main__":
    main()

