import chromadb

def create_db(path):
    client = chromadb.PersistentClient(path)
    collection = client.get_or_create_collection("notee")