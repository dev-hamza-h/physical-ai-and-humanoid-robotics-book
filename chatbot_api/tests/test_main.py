from fastapi.testclient import TestClient
from unittest.mock import patch
from chatbot_api.src.main import app

client = TestClient(app)

@patch('chatbot_api.src.main.rag_pipeline')
def test_query_endpoint(mock_rag_pipeline):
    # Arrange
    mock_rag_pipeline.retrieve_documents.return_value = ["doc1", "doc2"]
    mock_rag_pipeline.generate_answer.return_value = "mocked answer"

    # Act
    response = client.post("/query", json={"query": "test query"})

    # Assert
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["answer"] == "mocked answer"
    assert len(response_json["sources"]) == 2
    assert response_json["sources"][0]["text"] == "doc1"
