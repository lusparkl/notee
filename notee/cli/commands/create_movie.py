from notee.cli.utils.logs import send_process, send_success, send_warning
from notee.db.add_file import add_file_to_db
from notee.templates.movie import create_movie_note
from typing import Annotated
import typer

app = typer.Typer()

@app.command("movie")
def create_movie(title: Annotated[str, typer.Argument(help="Title and name for your movie note.")]):
    """Create movie review note"""
    send_process(f"Allright, creating note for {title} movie.")
    notes = typer.prompt("Write some of your notes about this movie", default="")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces", default="")
    rating = None
    while not rating:
        resp = typer.prompt("Enter rating for this movie from 0 to 10", default="")
        try:
            if int(resp) >=0 and int(resp) <= 10:
                rating = int(resp)
            elif resp == None:
                break
            else:
                send_warning("Please enter number from 0 to 10 to rate your movie.")
        except:
            send_warning("Please enter number from 0 to 10 to rate your movie.")
    
    text, path, date = create_movie_note(title, notes, tags, rating)
    add_file_to_db(text, path, date)
    send_success(f"Created note {title}")