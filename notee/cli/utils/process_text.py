from notee.cli.utils.config import get_config

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