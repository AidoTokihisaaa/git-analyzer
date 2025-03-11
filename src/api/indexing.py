from fastapi import APIRouter
from src.services.git_service import clone_repository, get_latest_commit
from services.indexing_service import index_repository

router = APIRouter()

@router.post("/the/repo/url/")
async def index_repo(repo_url: str, branch: str = "main"):
    repo_path = clone_repository(repo_url, branch)
    commit_sha = get_latest_commit(repo_path)
    response = index_repository(repo_path)
    return {"status": response, "latest_commit": commit_sha}
