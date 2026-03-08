import chromadb
import uuid

def add_file_to_db(text: str, path: str, created_at = None):
    client = chromadb.Client()
    collection = client.get_collection("notee")
    collection.add(id=uuid.uuid4(), documents=[text], metadatas=[{
        "path": path,
        "created_at": created_at
    }])