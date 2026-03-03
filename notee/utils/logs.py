from rich.text import Text
from rich import print

def send_success(text) -> None:
    message = Text(text, style="bold spring_green1")
    print(message)

def send_warning(text) -> None:
    message = Text(text, style="bold orange1")
    print(message)

def send_error(text) -> None:
    message = Text(text, style="bold deep_pink1")
    print(message)

def send_process(text) -> None:
    message = Text(text, style="italic slate_blue1")
    print(message)
