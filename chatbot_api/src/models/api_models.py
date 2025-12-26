from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class QueryRequest(BaseModel):
    query: str
    session_id: Optional[UUID] = None

class Source(BaseModel):
    text: str
    url: str
    similarity_score: Optional[float] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
