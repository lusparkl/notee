from notee.cli.utils.logs import send_success
from notee.cli.utils.config import get_config
from notee.cli.utils.scaner import scan
import typer

app = typer.Typer()

@app.command("scan")
def scan_folder():
    """Scan folder to add notes to the db if they're not already there."""
    config = get_config()
    notes_folder = config["patches"]["base_folder"]
    n_new_files = scan(notes_folder)
    send_success(f"Scanned your vault, added {n_new_files} new files to the db!")
