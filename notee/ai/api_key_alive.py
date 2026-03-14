from google import genai
import openrouter
import requests
import google
import openai

def openai_apikey_check(api_key: str) -> bool:
    client = openai.Client(api_key=api_key)
    try:
        client.models.list()
        return True
    except openai.AuthenticationError:
        return False

def gemini_apikey_check(api_key: str) -> bool:
    client = genai.Client(api_key=api_key)
    try:
        client.models.list()
        return True
    except google.genai.errors.ClientError:
        return False

def hackclub_apikey_check(api_key: str) -> bool:
    client = openrouter.OpenRouter(
        api_key=api_key,
        server_url="https://ai.hackclub.com/proxy/v1",
    )

    try:
        client.chat.send(model="google/gemini-2.5-flash",
            messages=[{"role": "user", "content": "Tell me a joke."}],
            max_tokens=5
        )
        return True
    except openrouter.errors.openrouterdefaulterror.OpenRouterDefaultError:
        return False

    


