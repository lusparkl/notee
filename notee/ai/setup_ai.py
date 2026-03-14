from notee.ai.api_key_alive import openai_apikey_check, gemini_apikey_check, hackclub_apikey_check
from notee.cli.utils.logs import send_process, send_error
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
import typer

def setup_ai() -> list:
    
    custom_style = Style.from_dict({
        "completion-menu": "bg:#1e1e1e #d4d4d4",         
        "completion-menu.completion": "bg:#2d2d2d #bbbbbb",
        "completion-menu.completion.current": "bg:#3a3a3a #ffffff bold underline", 
        "scrollbar.background": "bg:#121212",            
        "scrollbar.button": "bg:#444444",                
    })

    ai_providers = ["OpenAI", "Google Gemini", "HackClub API"]
    providers_completer = WordCompleter(ai_providers, ignore_case=True, match_middle=True)
    send_process("Choose your AI provider:")
    user_choise = prompt(">", completer=providers_completer, complete_while_typing=True, style=custom_style)

    if user_choise not in ai_providers:
        send_error("Don't have this one yet. Please choose between providers that already implemented.")
        setup_ai()
    
    match user_choise:
        case "OpenAI":
            send_process("Now enter your OpenAI api key:")
            api_key = typer.prompt(">")
            
            if not openai_apikey_check(api_key):
                setup_ai()

            return ["OpenAI", "gpt-4.1-mini-2025-04-14", api_key]

        case "Google Gemini":
            send_process("Now enter your Google Gemini api key:")
            api_key = typer.prompt(">")   

            if not gemini_apikey_check(api_key):
                setup_ai()

            return ["Google Gemini", "gemini-2.5-flash", api_key]

        case "HackClub API":
            send_process("Now enter your Hack Club api key:")
            api_key = typer.prompt(">")

            if not hackclub_apikey_check(api_key):
                setup_ai()

            return ["HackClub API", "google/gemini-2.5-flash", api_key] 
