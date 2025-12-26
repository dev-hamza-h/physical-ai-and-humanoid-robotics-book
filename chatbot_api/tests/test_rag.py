import unittest
from unittest.mock import patch, MagicMock
from chatbot_api.src.core.rag import RAG

class TestRAG(unittest.TestCase):

    @patch('chatbot_api.src.core.rag.chromadb.Client')
    @patch('chatbot_api.src.core.rag.SentenceTransformer')
    def test_retrieve_documents(self, mock_sentence_transformer, mock_chromadb_client):
        # Arrange
        mock_model = MagicMock()
        mock_model.encode.return_value.tolist.return_value = [0.1, 0.2, 0.3]
        mock_sentence_transformer.return_value = mock_model

        mock_collection = MagicMock()
        mock_collection.query.return_value = {'documents': [['doc1', 'doc2']]}
        mock_client = MagicMock()
        mock_client.get_collection.return_value = mock_collection
        mock_chromadb_client.return_value = mock_client

        rag = RAG()
        query = "test query"
        n_results = 2

        # Act
        documents = rag.retrieve_documents(query, n_results=n_results)

        # Assert
        mock_model.encode.assert_called_once_with(query)
        mock_collection.query.assert_called_once_with(
            query_embeddings=[[0.1, 0.2, 0.3]],
            n_results=n_results
        )
        self.assertEqual(documents, ['doc1', 'doc2'])

    @patch('chatbot_api.src.core.rag.chromadb.Client')
    @patch('chatbot_api.src.core.rag.SentenceTransformer')
    def test_generate_answer(self, mock_sentence_transformer, mock_chromadb_client):
        # Arrange
        rag = RAG()
        query = "test query"
        retrieved_docs = ["doc1", "doc2"]

        # Act
        answer = rag.generate_answer(query, retrieved_docs)

        # Assert
        self.assertIn("This is a dummy answer", answer)
        self.assertIn("doc1", answer)
        self.assertIn("doc2", answer)

if __name__ == '__main__':
    unittest.main()
