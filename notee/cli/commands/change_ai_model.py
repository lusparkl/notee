from notee.cli.utils.config import get_config, save_config
from notee.cli.utils.logs import send_success
from typing import Annotated
import typer

app = typer.Typer()

@app.command("change_ai_model")
def change_ai_model(model_name: Annotated[str, typer.Argument(help="Model name from official docs.")]):
    """Change your ai model from the default one. Please be careful, if you pick something wrong ai module might stop working till you change model to working one."""
    config = get_config()
    config["settings"]["AI_model"] = model_name
    save_config(config)
    send_success(f"Changed your AI model to the {model_name}. Make sure that it exists!")