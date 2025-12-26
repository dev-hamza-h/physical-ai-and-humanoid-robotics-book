# Chatbot API

This is the FastAPI backend for the RAG chatbot for the "Physical AI Humanoid Robotics Book".

## Installation

1.  Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the API

Run the API with `uvicorn`:
```bash
uvicorn src.main:app --reload
```
The API will be available at `http://localhost:8000`.

## Endpoints

### POST /query

This endpoint takes a user's query and returns a response from the RAG pipeline.

**Request Body:**
```json
{
  "query": "Your question about the book",
  "session_id": "optional-session-id"
}
```

**Response Body:**
```json
{
  "answer": "The answer to your question.",
  "sources": [
    {
      "text": "The source text from the book.",
      "url": "The URL to the source.",
      "similarity_score": 0.9
    }
  ]
}
```
