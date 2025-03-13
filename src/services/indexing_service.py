from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import os
from src.utils.logger import logger

def index_repository(repo_path: str):
    logger.info(f"📚 Indexation du code source dans {repo_path}...")

    documents = SimpleDirectoryReader(repo_path).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.save_to_disk(f"{repo_path}/index.json")

    return "✅ Indexation terminée"
