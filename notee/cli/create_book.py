from typer import Typer
import typer
from notee.cli.utils.logs import send_process, send_warning
from notee.templates.book import create_book_note


app = Typer()

@app.command("book")
def create_book(title: str):
    send_process(f"Alright, creating book with title {title}. Press ENTER to skip property.")
    author = typer.prompt("What is the author of the book?")
    notes = typer.prompt("Write some of your notes about book")
    tags = typer.prompt("Now enter tags for this file, separate them by spaces")
    rating = None
    while not rating:
        resp = typer.prompt("Enter rating for this book from 0 to 10")
        try:
            if int(resp) >=0 and int(resp) <= 10:
                rating = int(resp)
            elif resp == None:
                break
            else:
                send_warning("Please enter number from 0 to 10 to rate your book.")
        except:
            send_warning("Please enter number from 0 to 10 to rate your book.")
    
    create_book_note(title=title, author=author, notes=notes, tags=tags, rating=rating)
    