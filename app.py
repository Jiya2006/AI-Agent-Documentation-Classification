import gradio as gr

from document_processor import extract_text
from agent import document_classification_agent


def process_document(file):

    if file is None:
        return "Please upload a document.", "", "", ""

    try:

        # Extract text
        text = extract_text(file)

        if not text.strip():
            return "No readable text was found.", "", "", ""

        # AI Agent
        result = document_classification_agent(text)

        category = result.get("category", "Unknown")
        confidence = result.get("confidence", 0)
        reason = result.get("reason", "No explanation available.")

        return (
            category,
            f"{confidence}%",
            reason,
            text[:5000]
        )

    except Exception as e:

        return (
            "Error",
            "0%",
            str(e),
            ""
        )


interface = gr.Interface(

    fn=process_document,

    inputs=gr.File(
        label="📄 Upload Document",
        file_types=[".pdf", ".docx", ".txt"]
    ),

    outputs=[
        gr.Textbox(
            label="🏷️ Document Category"
        ),

        gr.Textbox(
            label="📊 Confidence"
        ),

        gr.Textbox(
            label="📝 Classification Reason",
            lines=4
        ),

        gr.Textbox(
            label="📃 Extracted Text",
            lines=15
        )
    ],

    title="🤖 AI Agent Documentation Classification System",

    description=(
        "Upload a PDF, DOCX, or TXT document. "
        "The AI agent analyzes the document using an LLM "
        "and automatically classifies it."
    )
)


interface.launch(share=True)