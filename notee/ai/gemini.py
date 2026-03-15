from notee.cli.utils.logs import send_error
from notee.db.query import get_context_for_ai
from notee.ai.api_key_alive import gemini_apikey_check
from notee.cli.utils.config import get_config
from google import genai

def gemini_request(query):
    config = get_config()
    api_key = config["settings"]["AI_api_key"]
    model = config["settings"]["AI_model"]
    client = genai.Client(api_key=api_key)

    if not gemini_apikey_check(api_key):
        send_error("Your Gemini api key is not valid. Please change it with <notee setup_ai>.")
        return
    
    responce = client.models.generate_content(
        model=model,
        contents=f"You are ai model that is connected to the CLI notes app. Your main goal is to give persise responces without water to user based on their notes related to question. This is notes: {get_context_for_ai(query)}. \n\n This is user request: {query}"
    )

    return responce.text