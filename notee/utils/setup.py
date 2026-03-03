from notee.utils.logs import send_success, send_process, send_error, send_warning
from notee.utils.disk_operations import create_config_file, is_folder_exists
from pathlib import Path
from typer import Typer
import configparser
import typer
 
app = Typer()
 
@app.command("setup")
def setup():
    config_path = create_config_file()
    config = configparser.ConfigParser()

    send_process("Now it's time to setup your notes folder(You'll be able to change it later)")
    path = typer.prompt("Enter folder path")
    exists = is_folder_exists(path)
    if not exists:
        send_error(f"Can't find folder {path}, please provide already created folder.")
        return
    
