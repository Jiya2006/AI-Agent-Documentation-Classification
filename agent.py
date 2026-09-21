from classifier import classify_document


def document_classification_agent(text):

    if not text or not text.strip():
        return {
            "category": "Other",
            "confidence": 0,
            "reason": "No readable document content was found."
        }

    # Limit very large documents
    text = text[:12000]

    # Send document to the LLM classifier
    result = classify_document(text)

    return result