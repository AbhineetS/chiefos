from agents.decorators import tool
import os

@tool
async def extract_text_from_pdf(filepath: str) -> str:
    """Extract text content from a local PDF file."""
    print(f"\n[Tool Execution: PDF Reader] Reading document at '{filepath}'")
    
    if os.path.exists(filepath):
        try:
            from pypdf import PdfReader
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
            
    # Mocked fallback if file does not exist
    return f"Mocked PDF content for {filepath}: Contains standard operational guidelines and financial summaries."
