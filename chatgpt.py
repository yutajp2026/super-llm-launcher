import gradio as gr
from openai import OpenAI
import time

def gpt(message, chat_history, key):
    global gpt_history
    if not key:
        gr.Warning("ChatGPT: API Keyを入力してください。")
        time.sleep(1)
        return "", chat_history
        
    if not message:
        gr.Warning("ChatGPT: プロンプトを入力してください。")
        time.sleep(1)
        return "", chat_history
        
    with open('gpt_api_key.txt', 'w') as f:
        f.write(key) 
    
    client = OpenAI(api_key=key)

    if not chat_history:
        gpt_history = [{"role": "user", "content": message}]
    else:
        gpt_history.append({"role": "user", "content": message})
    
    chat_history.append({"role": "user", "content": message})
    
    response = client.responses.create(
        model="gpt-6-luna",
        input=gpt_history,
        store=False,
    )


    chat_history.append({"role": "assistant", "content": response.output_text})

    gpt_history += response.output

    return "", chat_history