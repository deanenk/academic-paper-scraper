from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Author(BaseModel):
    name: str
    affiliation: Optional[str] = None

class SearchQuery(BaseModel):
    query: str
    max_results: Optional[int] = 10
    sources: Optional[List[str]] = None

class Paper(BaseModel):
    title: str
    authors: List[Author]
    abstract: str
    publication_date: Optional[datetime] = None
    source: str
    url: str
    doi: Optional[str] = None
    citations: Optional[int] = None
    keywords: Optional[List[str]] = None

class StorageResponse(BaseModel):
    success: bool
    message: str
    paper_id: Optional[str] = None