from notee.cli.create_book import app as book_app
from notee.cli.create_idea import app as idea_app
from notee.cli.create_movie import app as movie_app
from notee.cli.create_source import app as source_app
from notee.cli.create_todo import app as todo_app
from notee.cli.setup import app as setup_app
from typer import Typer

app = Typer()

app.add_typer(setup_app)
app.add_typer(book_app)
app.add_typer(idea_app)
app.add_typer(movie_app)
app.add_typer(source_app)
app.add_typer(todo_app)


if __name__ == "__main__":
    app()