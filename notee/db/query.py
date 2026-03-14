from notee.cli.utils.config import get_config
import chromadb


def search_in_db(query: str) -> list:
    config = get_config()
    db_path = config["settings"]["db_path"]
    client = chromadb.PersistentClient(db_path)
    collection = client.get_collection("notee")
    result = collection.query(query_texts=query, n_results=3)
    
    responce = []
    for metadata in result["metadatas"][0]:
        path = metadata["path"]
        responce.append(path)
    
    return responce

def get_context_for_ai(query: str) -> str:
    config = get_config()
    db_path = config["settings"]["db_path"]
    client = chromadb.PersistentClient(db_path)
    collection = client.get_collection("notee")
    result = collection.query(query_texts=query, n_results=5)
    context = ""
    for document in result["documents"][0]:
        context += document

    return context

