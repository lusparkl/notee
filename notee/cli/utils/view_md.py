from rich.console import Console
from rich.markdown import Markdown

def view_md_file(path):
    console = Console()
    custom_theme = {
        "markdown.header": "bold magenta",
        "markdown.code": "italic cyan",
        "markdown.item": "yellow",
    }

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    markdown = Markdown(text, justify="left", code_theme="dracula")
    console.print(markdown)