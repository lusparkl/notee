from notee.cli.utils.logs import send_error
from notee.ai.api_key_alive import openai_apikey_check
from notee.db.query import get_context_for_ai
from notee.cli.utils.config import get_config
import openai

def openai_request(query) -> str:
    config = get_config()
    api_key = config["settings"]["AI_api_key"]
    model = config["settings"]["AI_model"]
    client = openai.Client(api_key=api_key)

    if not openai_apikey_check(api_key):
        send_error("Your openAI api key is not valid. Please change it with <notee setup_ai>.")
        return

    responce = client.responses.create(
        model=model,
        input=query,
        instructions=f"You are ai model that is connected to the CLI notes app. Your main goal is to give persise responces without water to user based on their notes related to question. This is notes: {get_context_for_ai(query)}"
    )

    return responce.output_text
