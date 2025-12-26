from fastapi import FastAPI
from .models.api_models import QueryRequest, QueryResponse, Source
from .core.rag import rag_pipeline

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query", response_model=QueryResponse)
def submit_query(request: QueryRequest):
    retrieved_docs = rag_pipeline.retrieve_documents(request.query)
    answer = rag_pipeline.generate_answer(request.query, retrieved_docs)

    sources = [
        Source(
            text=doc,
            url="http://example.com",  # Placeholder URL
            similarity_score=0.9 # Placeholder score
        ) for doc in retrieved_docs
    ]

    return QueryResponse(
        answer=answer,
        sources=sources
    )
