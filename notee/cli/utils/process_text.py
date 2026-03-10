from notee.cli.utils.config import get_config
import re

def process_tags(tags: str):
    config = get_config()
    obsidian = config["settings"]["obsidian_mode"]
    
    separated = tags.split(" ")
    result = "Tags: "
    for tag in separated:
        if obsidian == "y":
            result += f" - [[{tag}]]"
        else:
            result += f"#{tag} "
    
    return result

def process_links(links: str):
    separated = links.split(" ")
    result = ""
    for link in separated:
        result += f"{link} \n"
    
    return result

def process_if_exists(cond, text):
    if cond:
        return text
    return ""

def convert_obsidian_tags(text):
    pattern = r"\[\[(.*?)\]\]"

    def replace_with_hash(match):
        tag = match.group(1).strip()
        return f"#{tag}"

    return re.sub(pattern, replace_with_hash, text)