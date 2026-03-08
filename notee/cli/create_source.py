from notee.cli.utils.logs import send_process, send_success
from notee.templates.source import create_source_note
from notee.db.add_file import add_file_to_db
from typing import Annotated
import typer

app = typer.Typer()

@app.command("source")
def create_source(title: Annotated[str, typer.Argument(help="Title and name for your source note.")]):
    """Create note with source for smth"""
    send_process(f"Allright, creating note for {title} source.")
    notes = typer.prompt("Write some of your notes about this source", default="")
    links = typer.prompt("Write links to this source, separate them by space too", default="")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces", default="")
    
    text, path, date = create_source_note(title, notes, tags, links)
    add_file_to_db(text, path, date)
    send_success(f"Created note {title}")