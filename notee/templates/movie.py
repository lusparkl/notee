from notee.cli.utils.process_text import process_tags, process_if_exists
from notee.cli.utils.config import get_config
from mdutils.fileutils.fileutils import MarkDownFile
from datetime import datetime

def create_movie_note(title: str, notes: str = None, tags: str = None, rating: int = None):
    data = f"""
{datetime.now().strftime("%Y-%m-%d %H:%M")}
{process_tags(tags) if tags else ""}

# {title}

{process_if_exists(notes, notes)}

{process_if_exists(rating, f"**{rating}/10⭐**")}
"""
    config = get_config()
    file = MarkDownFile(name=title, dirname=config["patches"]["movie"])
    file.append_end(data)

