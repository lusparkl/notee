from notee.cli.utils.config import get_config
import chromadb

def get_file_pathes() -> list:
    config = get_config()
    db_path = config["settings"]["db_path"]
    client = chromadb.PersistentClient(db_path)
    collection = client.get_collection("notee")
    result = collection.get(include=["metadatas"], limit=10000)
    pathes = []
    for metadata in result["metadatas"]:
        pathes.append(metadata["path"])

    return pathes


