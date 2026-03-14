from notee.cli.utils.config import get_config, save_config
from notee.cli.utils.logs import send_success
from notee.ai.setup_ai import setup_ai
import typer

app = typer.Typer()

@app.command("setup_ai")
def change_ai_setup():
    """Change AI provider/api key"""
    config = get_config()
    provider, model, api_key = setup_ai()
    config["settings"]["AI_module"] = "y"
    config["settings"]["AI_provider"] = provider
    config["settings"]["AI_model"] = model
    config["settings"]["AI_api_key"] = api_key

    send_success("AI setup finished!")
    save_config(config)