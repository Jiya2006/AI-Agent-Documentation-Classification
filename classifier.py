import json
from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


def classify_document(text):

    prompt = f"""
You are an AI document classification agent.

Analyze the document and classify it into exactly ONE of these categories:

1. Resume / CV
2. Research Paper
3. Invoice
4. Certificate
5. Academic Report / Assignment
6. Other

Return ONLY valid JSON in this exact structure:

{{
    "category": "one category from the list",
    "confidence": 0,
    "reason": "short explanation"
}}

Rules:
- category must be one of the six categories.
- confidence must be a number between 0 and 100.
- reason should briefly explain why the document belongs to that category.
- Do not include Markdown.
- Do not include any text outside the JSON.

DOCUMENT:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are an intelligent document classification assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "category": "Other",
            "confidence": 0,
            "reason": "The model returned an invalid classification format."
        }