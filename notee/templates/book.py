from notee.cli.utils.process_text import process_tags, process_if_exists
from notee.cli.utils.config import get_config
from mdutils.fileutils.fileutils import MarkDownFile
from datetime import datetime

def create_book_note(title: str, author: str = None, notes: str = None, tags: str = None, rating: int = None):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    data = f"""
{date}
{process_tags(tags) if tags else ""}

# {title}

{process_if_exists(author, f"By **{author}**")}

## Notes

{process_if_exists(notes, notes)}

{process_if_exists(rating, f"**{rating}/10⭐**")}
"""
    config = get_config()
    file = MarkDownFile(name=title, dirname=config["patches"]["book"])
    file.append_end(data)

    return [data, f"{config["patches"]["book"]}/{title}.md", date]

