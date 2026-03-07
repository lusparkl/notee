from notee.cli.utils.process_text import process_tags
from mdutils.fileutils.fileutils import MarkDownFile
from notee.cli.utils.config import get_config
from datetime import datetime

def create_todo_note(title, description: str = None, tags: str = None):
    data = f"""
{datetime.now().strftime("%Y-%m-%d %H:%M")}
{process_tags(tags) if tags else ""}

# {title}

{description}
"""
    config = get_config()
    file = MarkDownFile(name=title, dirname=config["patches"]["todo"])
    file.append_end(data)