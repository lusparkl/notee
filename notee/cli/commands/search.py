from notee.cli.utils.logs import send_success, send_warning
from notee.cli.utils.view_md import view_md_file
from notee.db.query import search_in_db
from rich.console import Console
from InquirerPy import inquirer
from typing import Annotated
import typer

app = typer.Typer()

@app.command("search")
def search(query: Annotated[str, typer.Argument(help="Query for your search request")]):
    """Search for your note by query"""
    console = Console()

    with console.status(" ", spinner="dots"):
        responce = search_in_db(query)
    if not responce:
        send_warning("Can't find anything😢 Try another query.")
        return
    
    responce.append("Exit")
    send_success("Here is your notes:")
    choice = inquirer.select(message="Select please", choices=responce, default="Exit").execute()
    
    if choice == "Exit":
        return
    
    view_md_file(choice)

