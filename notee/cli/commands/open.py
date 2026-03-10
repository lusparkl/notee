from notee.cli.utils.logs import send_error, send_process
from prompt_toolkit.completion import WordCompleter
from notee.db.get_file_patches import get_file_pathes
from notee.cli.utils.view_md import view_md_file
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
import typer

app = typer.Typer()

@app.command("open")
def open_note():
    """Open some note in terminal"""
    
    custom_style = Style.from_dict({
        "completion-menu": "bg:#1e1e1e #d4d4d4",         
        "completion-menu.completion": "bg:#2d2d2d #bbbbbb",
        "completion-menu.completion.current": "bg:#3a3a3a #ffffff bold underline", 
        "scrollbar.background": "bg:#121212",            
        "scrollbar.button": "bg:#444444",                
    })

    pathes = get_file_pathes()
    pathes_completer = WordCompleter(pathes, ignore_case=True, match_middle=True)
    send_process("Enter path for your note:")
    user_choise = prompt(">", completer=pathes_completer, complete_while_typing=True, style=custom_style)
    
    if user_choise not in pathes:
        send_error("Can't find this path in db. Please use <notee scan> and try again.")
        return
        
    view_md_file(user_choise)

