import unittest
from chatbot_api.src.core.rag import RAG
import chromadb
import shutil

class TestRAGIntegration(unittest.TestCase):

    def setUp(self):
        # Use an in-memory or a temporary on-disk instance of ChromaDB for testing
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("test_collection")
        self.rag = RAG()
        self.rag.collection = self.collection

        # Add some dummy data
        self.docs = ["This is a document about cats.", "This is a document about dogs."]
        self.rag.collection.add(
            documents=self.docs,
            ids=["doc1", "doc2"]
        )

    def test_full_rag_pipeline(self):
        # This is a simple integration test that checks if the pipeline can retrieve documents.
        # A more complete test would also check the answer generation.
        
        # Act
        retrieved_docs = self.rag.retrieve_documents("What are cats?", n_results=1)

        # Assert
        self.assertIn("This is a document about cats.", retrieved_docs)

    def tearDown(self):
        # Clean up the test collection
        self.client.delete_collection(name="test_collection")


if __name__ == '__main__':
    unittest.main()
