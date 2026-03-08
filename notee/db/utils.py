def get_name_from_path(path: str) -> str:
    separated = path.split("/")
    return separated[-1].replace(".md", "")

