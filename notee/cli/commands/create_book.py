from notee.cli.utils.logs import send_process, send_warning, send_success
from notee.templates.book import create_book_note
from notee.db.add_file import add_file_to_db
from typing import Annotated
import typer

app = typer.Typer()

@app.command("book")
def create_book(title: Annotated[str, typer.Argument(help="Title and name for your book note.")]):
    """
    Create book review note
    """
    send_process(f"Alright, creating book with title {title}.")
    author = typer.prompt("What is the author of the book?", default="")
    notes = typer.prompt("Write some of your notes about book", default="")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces", default="")
    rating = None
    while not rating:
        resp = typer.prompt("Enter rating for this book from 0 to 10", default="")
        try:
            if int(resp) >=0 and int(resp) <= 10:
                rating = int(resp)
            elif resp == None:
                break
            else:
                send_warning("Please enter number from 0 to 10 to rate your book.")
        except:
            send_warning("Please enter number from 0 to 10 to rate your book.")
    
    text, path, date = create_book_note(title, author, notes, tags, rating)
    add_file_to_db(text, path, date)
    send_success(f"Created note {title}")
    