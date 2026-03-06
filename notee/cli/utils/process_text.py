def process_tags(tags: str):
    separated = tags.split(" ")
    result = "Tags: "
    for tag in separated:
        result += f" - [[{tag}]]"
    
    return result

def process_if_exists(cond, text):
    if cond:
        return text
    return ""