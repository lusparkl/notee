from notee.cli.utils.logs import send_process, send_success, send_warning
from notee.db.query import search_in_db
from typing import Annotated
import typer

app = typer.Typer()

@app.command("search")
def search(query: Annotated[str, typer.Argument(help="Query for your search request")]):
    """Search for your note by query"""
    responce = search_in_db(query)
    if not responce:
        send_warning("Can't find anything😢 Try another query.")
        return
    
    send_success("Here is your notes:")
    for path in responce:
        send_process(path)

