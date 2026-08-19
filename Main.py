import openai

client = openai.OpenAI(
    base_url="http://poopy.local:8080/v1",
    api_key="not-needed"
)
while True:
    print(">>> ", end="", flush=True)
    text = input()
    if text=="/bye":
        break
    response = client.chat.completions.create(
        model = "Qwen3-4B-Q4_K_M",
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