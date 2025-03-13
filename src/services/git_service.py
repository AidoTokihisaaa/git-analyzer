import pygit2
import os
import shutil
from src.config import REPO_BASE_PATH
from src.utils.logger import logger

EXCLUDED_FOLDERS = [".git", "node_modules", "__pycache__", "dist", "build", ".venv"]

def clone_repository(repo_url: str, branch: str = "main") -> str:
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPO_BASE_PATH, repo_name)

    if os.path.exists(repo_path):
        logger.info(f"✅ Le repo {repo_name} est déjà cloné.")
        return repo_path  

    logger.info(f"🌀 Clonage du repo {repo_url} sur la branche {branch}...")
    repo = pygit2.clone_repository(repo_url, repo_path, checkout_branch=branch)

    logger.info("🧹 Nettoyage des fichiers inutiles...")
    for folder in EXCLUDED_FOLDERS:
        folder_path = os.path.join(repo_path, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

    return repo_path

def get_latest_commit(repo_path: str) -> str:
    repo = pygit2.Repository(repo_path)
    return repo.head.target.hex
