import tempfile
import os

def process_txt(file_path, collection):
    try:
        # Read the content of the text file with UTF-8 encoding
        with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
            content = file.read()

        # Print the content of the text file
        print(content)

        # Add the document to the ChromaDB collection
        collection.add(
            documents=[content],
            metadatas=[{"filename": os.path.basename(file_path)}],
            ids=[os.path.basename(file_path)]
        )

        return True
    except Exception as e:
        print(f"Error processing text file: {str(e)}")
        return False
