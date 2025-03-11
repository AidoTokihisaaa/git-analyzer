from fastapi import APIRouter
from src.services.vector_db import search_repository

router = APIRouter()

@router.get("/the/repo/url/")
async def search_repo(query: str):
    results = search_repository(query)
    return {"search_results": results}
