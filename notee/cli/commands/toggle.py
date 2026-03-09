from notee.cli.utils.logs import send_success, send_process, send_error
from notee.cli.utils.config import get_config, save_config
from pathlib import Path
import typer

app = typer.Typer()

app.command("obsidian_mode")
def togle_obsidian_mode(
        on: bool = typer.Option(None, "--on", help="Enable obsidian mode."),
        off: bool = typer.Option(None, "--off", help="Disable obsidian mode.")
):
    """Toggle between creating notes for obsidian or regular md format.
    --on - Enable obsidian mode
    --off - Disable obsidian mode
    """
    if bool(on) == bool(off):
        send_error("Use only --on or --off flags please.")
        return
    
    config = get_config()

    if on:
        config["settings"]["obsidian_mode"] = "y"
        save_config(config)
        send_success("Enabled obsidian mode🥳")
    else:
        config["settings"]["obsidian_mode"] = "n"
        save_config(config)
        send_success("Disabled obsidian mode👌")

app.command("different_folders")
def togle_different_folders(
        on: bool = typer.Option(None, "--on", help="Enable different folders."),
        off: bool = typer.Option(None, "--off", help="Disable different folders.")
):
    """Togle between creating folder for each tipe of template or store all notes in core folder.
    --on - Enable different folders.
    --off - Disable different folders.
    """

    if bool(on) == bool(off):
        send_error("Use only --on or --off flags please.")
        return

    TEMPLATES = ["book", "idea", "movie", "source", "todo"]
    config = get_config()
    base_path = config["patches"]["base_folder"]

    if on:
        for template in TEMPLATES:
            template_folder_path = Path(f"{base_path}/{template}")
            template_folder_path.touch()
            config["patches"][template] = f"{base_path}/{template}"
            send_success("Enabled different folders. Your notes will be saving into different folders from now.")
    else:
        for template in TEMPLATES:
            config["patches"][template] = base_path
            send_success("Disabled different folders. Your notes will be saving into base folder from now.")
    
    save_config(config)