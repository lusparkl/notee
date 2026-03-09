from notee.db.add_file import add_file_to_db
from notee.db.get_file_patches import get_file_pathes
import os

def add_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
        add_file_to_db(text, path)
        file.close()

def scan(folder_path: str):
    names = get_file_pathes()
    n_new_files = 0
    with os.scandir(folder_path) as directory:
        for entity in directory:
            if entity.is_dir():
                n_new_files += scan(entity.path)
            else:
                if entity.path not in names:
                    add_from_file(entity.path)
                    n_new_files += 1
    return n_new_files
    
