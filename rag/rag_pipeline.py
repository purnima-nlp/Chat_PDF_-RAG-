from rag.retriever import Retriever
from rag.prompt_builder import build_prompt
from llm_clients.openai_client import ask_openai


class RAGPipeline:
    def __init__(self, top_k=5):
        self.retriever = Retriever(top_k)

    def ask(self, query):
        chunks = self.retriever.retrieve(query)
        prompt = build_prompt(query, chunks)
        answer = ask_openai(prompt)
        return answer


if __name__ == "__main__":
    rag = RAGPipeline()
    print(rag.ask("Summarize the main contribution of the paper"))

