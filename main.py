import os

import openai
from dotenv import load_dotenv

load_dotenv()

local_client = openai.OpenAI(
    base_url="http://poopy.local:8080/v1",
    api_key="not-needed"
)

open_router_client = openai.OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
)
while True:
    print(">>> ", end="", flush=True)
    text = input()
    if text=="/bye":
        break
    response = open_router_client.chat.completions.create(
        model = "qwen/qwen3-8b",
        messages = [
            {"role": "user", "content": text}
        ],
        stream = True
    )

    for chunk in response:
        reply = chunk.choices[0].delta.content
        if reply:
            print(reply, end="", flush=True)

    print()
