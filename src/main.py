from fastapi import FastAPI
from src.api.indexing import router as indexing_router
from src.api.search import router as search_router

app = FastAPI(title="Git Repository Analyzer")

app.include_router(indexing_router, prefix="/index")
app.include_router(search_router, prefix="/search")

@app.get("/")
def home():
    return {"message": "Git Repository Analyzer is running!"}
