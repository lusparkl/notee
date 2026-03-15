from notee.cli.utils.process_text import process_tags, process_if_exists, process_links
from notee.cli.utils.config import get_config
from mdutils.fileutils.fileutils import MarkDownFile
from datetime import datetime

def create_source_note(title: str, notes: str = None, tags: str = None, links: str = None):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    data = f"""
{date}
{process_tags(tags) if tags else ""}

# {title}

{process_if_exists(notes, notes)}

## Links

{process_links(links) if links else ""}
"""
    config = get_config()
    file = MarkDownFile(name=title, dirname=config["patches"]["source"])
    file.append_end(data)

    return [data, f"{config["patches"]["source"]}/{title}.md", date]

