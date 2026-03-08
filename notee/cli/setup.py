from notee.cli.utils.logs import send_success, send_process, send_error, send_warning
from notee.cli.utils.disk_operations import create_config_file, is_folder_exists
from notee.db.create_db import create_db
from pathlib import Path
from typer import Typer
import configparser
import typer
 
app = Typer()
 
@app.command("setup")
def setup():
    """Setup notee before using it."""
    create_db()
    config_path = create_config_file()
    config = configparser.ConfigParser()
    config["patches"] = {}
    config.add_section("settings")
    TEMPLATES = ["book", "idea", "movie", "source", "todo"]

    send_process("Now it's time to setup your notes folder.")
    path = typer.prompt("Enter folder path")
    exists = is_folder_exists(path)
    if not exists:
        send_error(f"Can't find folder {path}, please provide already created folder.")
        return
    
    config["patches"]["base_folder"] = path
    send_process("Create different folders for each temlate type?")
    different_folders = typer.confirm("Create different folders?")
    
    if different_folders:
        for template in TEMPLATES:
            template_folder_path = Path(f"{path}/{template}")
            template_folder_path.touch()
            config["patches"][template] = f"{path}/{template}"
    else:
        for template in TEMPLATES:
            config["patches"][template] = path
    
    send_process("Create notes with default MD or for obsidian? (You can change it later)")
    obsidian_mode = typer.confirm("Use obsidian mode?")

    if obsidian_mode:
        config["settings"]["obsidian_mode"] = "y"
    else:
        config["settings"]["obsidian_mode"] = "n"
    
    with open(config_path, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    send_success("Finished setup! Use <notee --help> to get all commands")
