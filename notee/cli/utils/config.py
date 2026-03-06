import typer
import configparser
from pathlib import Path

def get_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    app_dir = typer.get_app_dir("notee")
    config_path = Path(app_dir) / "config.ini"

    if not config_path.exists():
        raise FileNotFoundError("Can't find config. Please use <notee setup> to create it.")

    config.read(config_path, encoding="utf-8")
    return config


def save_config(config: configparser.ConfigParser) -> None:
    app_dir = typer.get_app_dir("notee")
    config_path = Path(app_dir) / "config.ini"
    
    with open(config_path, "w", encoding="utf-8") as configfile:
        config.write(configfile)