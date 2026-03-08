import chromadb

def get_file_names() -> list:
    client = chromadb.Client()
    collection = client.get_collection("notee")
    result = collection.get(include=["metadatas"], limit=10000)
    names = []
    for metadata in result["metadatas"]:
        names.append(f"{metadata["name"]}.md")

    return names