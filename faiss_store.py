import faiss
import pickle
import numpy as np


INDEX_PATH = "vector.index"
META_PATH = "metadata.pkl"


class FaissStore:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)

        with open(META_PATH, "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query_vector, top_k=5):
        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results

