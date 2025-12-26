import os
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Initialize ChromaDB client and create a collection
client = chromadb.Client()
collection = client.create_collection("book_content")

# 2. Initialize the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Walk through the docs directory and read all markdown files
def get_all_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                yield os.path.join(root, file)

# 4. Read the content of each file and split it into chunks (paragraphs)
def get_chunks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple split by paragraph, can be improved with more sophisticated chunking
    chunks = content.split('\n\n')
    return [chunk for chunk in chunks if chunk.strip()]

# 5. Process all markdown files, create embeddings, and store them in ChromaDB
def index_content():
    doc_id = 0
    for file_path in get_all_markdown_files('docs'):
        chunks = get_chunks(file_path)
        for chunk in chunks:
            embedding = model.encode(chunk).tolist()
            collection.add(
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"source": file_path}],
                ids=[str(doc_id)]
            )
            doc_id += 1
    print(f"Indexed {doc_id} chunks.")

if __name__ == "__main__":
    index_content()
