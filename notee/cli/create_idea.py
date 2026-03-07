from notee.cli.utils.logs import send_process, send_success
from notee.templates.idea import create_idea_note
from typing import Annotated
import typer

app = typer.Typer()

@app.command("idea")
def create_idea(title: Annotated[str, typer.Argument(help="Title and name for your idea note.")]):
    """Create idea note"""
    send_process(f"Alright, creating idea note '{title}'.")
    description = typer.prompt("Describe your idea", default="")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces", default="")

    create_idea_note(title, description, tags)
    send_success(f"Created note {title}")

