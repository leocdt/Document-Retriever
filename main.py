import os
import streamlit as st
import chromadb
from pdf import process_pdf
from md import process_md
from txt import process_txt

# Initialize ChromaDB client
client = chromadb.Client()

# Create or get a collection
collection = client.get_or_create_collection("documents")

# Set up the Streamlit app
st.title("Document Upload and Vector Database")
st.write("Upload a document to add it to the ChromaDB Vector database.")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "md"])

def save_uploaded_file(uploaded_file, file_type):
    # Create the data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Create the subdirectory for the file type if it doesn't exist
    subdir = os.path.join("data", file_type)
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    
    # Save the file
    file_path = os.path.join(subdir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

if uploaded_file is not None:
    # Process the file based on its type or extension
    file_type = uploaded_file.type
    file_extension = uploaded_file.name.split('.')[-1].lower()

    if file_type == "application/pdf" or file_extension == "pdf":
        file_path = save_uploaded_file(uploaded_file, "pdf")
        success = process_pdf(file_path, collection)
    elif file_type == "text/markdown" or file_extension == "md":
        file_path = save_uploaded_file(uploaded_file, "md")
        success = process_md(file_path, collection)
    elif file_type == "text/plain" or file_extension == "txt":
        file_path = save_uploaded_file(uploaded_file, "txt")
        success = process_txt(file_path, collection)
    else:
        st.error("Unsupported file type.")
        success = False

    if success:
        st.success(f"Document successfully added to the vector database and saved in {file_path}!")
    else:
        st.error("Failed to process the document.")

# Display the current documents in the database
st.subheader("Documents in the Database")
documents = collection.get()
for idx, doc in enumerate(documents['metadatas']):
    st.write(f"{idx + 1}. {doc['filename']}")

# Add some styling
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)
