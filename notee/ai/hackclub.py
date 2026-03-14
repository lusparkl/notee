from notee.ai.api_key_alive import hackclub_apikey_check
from notee.db.query import get_context_for_ai
from notee.cli.utils.config import get_config
from notee.cli.utils.logs import send_error
from openrouter import OpenRouter

def hackclub_request(query):
    config = get_config()
    api_key = config["settings"]["AI_api_key"]
    model = config["settings"]["AI_model"]
    client = OpenRouter(
        api_key=api_key,
        server_url="https://ai.hackclub.com/proxy/v1",
    )

    if not hackclub_apikey_check(api_key):
        send_error("Your HackClub api key is not valid. Please change it with <notee change_api_key>.")

    response = client.chat.send(
        model=model,
        messages=[
            {"role": "user", "content": query},
            {"role": "system", "content": f"You are ai model that is connected to the CLI notes app. Your main goal is to give persise responces without water to user based on their notes related to question. This is notes: {get_context_for_ai(query)}"}
        ],
        stream=False,
    )

    return response.choices[0].message.content
    





