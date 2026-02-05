from rag.retriever import Retriever
from rag.prompt_builder import build_prompt
from llm_clients.openai_client import ask_openai
from llm_clients.gemini_client import ask_gemini


class RAGPipeline:
    def __init__(self, top_k=5, provider="openai"):
        self.retriever = Retriever(top_k)
        self.provider = provider

    def ask(self, query):
        chunks = self.retriever.retrieve(query)
        prompt = build_prompt(query, chunks)

        if self.provider == "gemini":
            return ask_gemini(prompt)
        else:
            return ask_openai(prompt)


if __name__ == "__main__":
    rag = RAGPipeline(provider="gemini")   # or "openai"
    print(rag.ask("What problem does the paper solve?"))
