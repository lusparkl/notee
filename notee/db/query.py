from notee.db.utils import get_name_from_path
import chromadb


def search_in_db(query: str) -> list:
    client = chromadb.Client()
    collection = client.get_collection("notee")
    result = collection.query(query_texts=query, n_results=5)
    
    responce = []
    for metadata in result["metadatas"]:
        path = metadata["path"]
        name = get_name_from_path(path)
        responce.append({"name": name, "path": path})
    
    return responce