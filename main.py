from rag.rag_pipeline import RAGPipeline


def main():
    print("\n📚 PDF RAG Chat (type 'exit' to quit)\n")

    provider = input("Choose model (openai/gemini) [openai]: ").strip().lower()
    if provider not in ["openai", "gemini"]:
        provider = "openai"

    rag = RAGPipeline(provider=provider)

    while True:
        query = input("\nAsk > ").strip()

        if query.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        try:
            answer = rag.ask(query)
            print("\nAnswer:\n", answer)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

