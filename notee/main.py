from notee.cli.commands.create_book import app as book_app
from notee.cli.commands.create_idea import app as idea_app
from notee.cli.commands.create_movie import app as movie_app
from notee.cli.commands.create_source import app as source_app
from notee.cli.commands.create_todo import app as todo_app
from notee.cli.commands.setup import app as setup_app
from notee.cli.commands.search import app as search_app
from notee.cli.commands.toggle import app as togle_app
from notee.cli.commands.scan import app as scan_app
from typer import Typer

app = Typer()

app.add_typer(setup_app)
app.add_typer(book_app)
app.add_typer(idea_app)
app.add_typer(movie_app)
app.add_typer(source_app)
app.add_typer(todo_app)
app.add_typer(search_app)
app.add_typer(togle_app)
app.add_typer(scan_app)


if __name__ == "__main__":
    app()