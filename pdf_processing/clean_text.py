import re


def clean_text(text: str) -> str:
    """
    Basic cleanup for extracted PDF text.
    """
    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"-\s+", "", text)

    return text.strip()


def clean_documents(documents: list) -> list:
    cleaned = []
    for doc in documents:
        cleaned.append({
            "source": doc["source"],
            "text": clean_text(doc["text"])
        })
    return cleaned


if __name__ == "__main__":
    sample = "This is   a test \n text - broken"
    print(clean_text(sample))

