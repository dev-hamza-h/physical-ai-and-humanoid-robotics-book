import chromadb
from sentence_transformers import SentenceTransformer

class RAG:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_collection("book_content")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def retrieve_documents(self, query: str, n_results: int = 5):
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results['documents'][0]

    def generate_answer(self, query: str, retrieved_docs: list):
        # In a real implementation, this would use an LLM to generate an answer
        # based on the query and the retrieved documents.
        # For now, we'll just return a formatted string of the retrieved docs.
        return "This is a dummy answer based on the following documents:\n\n" + "\n\n".join(retrieved_docs)

rag_pipeline = RAG()

