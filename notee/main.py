from notee.cli.create_book import app as book_app
from notee.cli.setup import app as setup_app
from typer import Typer

app = Typer()

app.add_typer(setup_app)
app.add_typer(book_app)


if __name__ == "__main__":
    app()