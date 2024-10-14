import tempfile
import os

def process_md(file_path, collection):
    try:
        # Read the content of the Markdown file
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read()

        # Print the content of the Markdown file
        print(content)

        # Add the document to the ChromaDB collection
        collection.add(
            documents=[content],
            metadatas=[{"filename": os.path.basename(file_path)}],
            ids=[os.path.basename(file_path)]
        )

        return True
    except Exception as e:
        print(f"Error processing Markdown: {str(e)}")
        return False
