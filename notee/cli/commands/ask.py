from notee.ai.hackclub import hackclub_request
from notee.cli.utils.config import get_config
from notee.cli.utils.logs import send_error
from notee.ai.gemini import gemini_request
from notee.ai.openai import openai_request
from typing import Annotated
import typer

app = typer.Typer()

@app.command("ask")
def ask(query: Annotated[str, typer.Argument(help="Query for your request.")]):
    config = get_config()
    
    if config["settings"]["AI_module"] == "n":
        send_error("Your ai module isn't setup yet. Use <notee setup_ai> to use this command.")
        return
    
    ai_provider = config["settings"]["AI_provider"]
    match ai_provider:
        case "OpenAI":
            print(openai_request(query))
            return
        case "Google Gemini":
            print(gemini_request(query))
            return
        case "HackClub API":
            print(hackclub_request(query))
            return 
        
    send_error("Something wrong happened. Try to setup your ai module settings with <notee setup_ai>")