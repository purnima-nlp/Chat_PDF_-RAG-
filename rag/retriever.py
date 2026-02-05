from embeddings.embedder import embed_query
from faiss_store import FaissStore


class Retriever:
    def __init__(self, top_k=5):
        self.store = FaissStore()
        self.top_k = top_k

    def retrieve(self, query):
        query_vec = embed_query(query)
        results = self.store.search(query_vec, self.top_k)
        return results


if __name__ == "__main__":
    r = Retriever()
    res = r.retrieve("What is thermal super resolution?")
    for chunk in res:
        print(chunk["text"][:200])

