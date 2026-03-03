from pathlib import Path
import typer

def is_folder_exists(path):
    return Path(path).is_dir()

def create_config_file() -> str:
    app_dir = typer.get_app_dir("streak_saver")
    config_path = Path(app_dir) / "config.ini"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    Path.touch(config_path)

    return config_path