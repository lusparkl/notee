from notee.cli.utils.logs import send_process, send_success
from notee.templates.todo import create_todo_note
from notee.db.add_file import add_file_to_db
from typing import Annotated
import typer

app = typer.Typer()

@app.command("todo")
def create_idea(title: Annotated[str, typer.Argument(help="Title and name for your todo note.")]):
    """Create todo note"""
    send_process(f"Alright, creating todo note '{title}'.")
    description = typer.prompt("Describe what you need to do", default="")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces", default="")

    text, path, date = create_todo_note(title, description, tags)
    add_file_to_db(text, path, date)
    send_success(f"Created note {title}")
