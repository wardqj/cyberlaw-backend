
from fastapi import APIRouter, Request
from services.search_service import search_articles
from pydantic import BaseModel

router = APIRouter()

class SearchQuery(BaseModel):
    query: str

@router.post("/")
async def search(query: SearchQuery):
    results = search_articles(query.query)
    return {"results": results}
