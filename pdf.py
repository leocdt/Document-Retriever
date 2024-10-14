import tempfile
import os
from PyPDF2 import PdfReader

def process_pdf(file_path, collection):
    try:
        # Read the content of the PDF file
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            content = ""
            for page in pdf_reader.pages:
                content += page.extract_text()

        # Add the document to the ChromaDB collection
        collection.add(
            documents=[content],
            metadatas=[{"filename": os.path.basename(file_path)}],
            ids=[os.path.basename(file_path)]
        )

        return True
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False
