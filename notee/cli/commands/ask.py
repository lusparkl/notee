from notee.ai.hackclub import hackclub_request
from notee.cli.utils.config import get_config
from notee.cli.utils.logs import send_error
from notee.ai.gemini import gemini_request
from notee.ai.openai import openai_request
from rich.console import Console
from typing import Annotated
import typer

app = typer.Typer()

@app.command("ask")
def ask(query: Annotated[str, typer.Argument(help="Query for your request.")]):
    """Ask AI question and it'll answer it based on your notes."""
    console = Console()

    with console.status(" ", spinner="dots"):
        config = get_config()
    
        if config["settings"]["AI_module"] == "n":
            send_error("Your ai module isn't setup yet. Use <notee setup_ai> to use this command.")
            return
    
        ai_provider = config["settings"]["AI_provider"]
        match ai_provider:
            case "OpenAI":
                responce = openai_request(query)
            case "Google Gemini":
                responce = gemini_request(query)
            case "HackClub API":
                responce = hackclub_request(query)
            case _ :
                send_error("Something wrong happened. Try to setup your ai module again with <notee setup_ai>.")
            
        print(responce)
        
    