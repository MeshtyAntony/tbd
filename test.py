import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPEN_ROUTER_API_KEY")

print("OpenRouter API Key:", api_key)