from pymilvus import connections, Collection
from config import MILVUS_HOST, MILVUS_PORT
from utils.logger import logger

connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
collection = Collection("git_repo_chunks")

def search_repository(query_text: str):
    search_results = collection.search([query_text], "embedding", limit=5)
    return search_results
