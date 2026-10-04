from google import genai

def gemini(message, chat_history, key):
    if not message:
        return "プロンプトを入力してください。", chat_history
    
    if not key:
        return "API keyを入力してください。", chat_history
    
    with open('gemini_api_key.txt', 'w') as f:
        f.write(key)

    client = genai.Client(api_key=key)

    history = [
        {
            "type": "user_input",
            "content": [{"type": "text", "text": message}],
        }
    ]

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=history,
    )

    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": interaction.steps[-1].content[0].text})

    for step in interaction.steps:
        history.append(step.model_dump())
    
    return "", chat_history