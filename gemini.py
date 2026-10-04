import gradio as gr
from google import genai
import time

def gemini(message, chat_history, key):

    if not key:
        gr.Warning("Gemini: API Keyを入力してください。")
        time.sleep(1)
        return "", chat_history
    
    if not message:
        gr.Warning("Gemini: プロンプトを入力してください。")
        time.sleep(1)
        return "", chat_history
    
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