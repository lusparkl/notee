import chromadb

def create_db():
    client = chromadb.Client()
    collection = client.get_or_create_collection("notee")