from openai import OpenAI
import gradio as gr
import time

def llama(message, chat_history, key):
    global llama_history
    if not key:
        gr.Warning("Llama: API Keyを入力してください。")
        time.sleep(1)
        return "", chat_history
        
    if not message:
        gr.Warning("Llama: プロンプトを入力してください。")
        time.sleep(1)
        return "", chat_history
    
    with open('groq_api_key.txt', 'w') as f:
        f.write(key) 

    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1",
    )

    if not chat_history:
        llama_history = [{"role": "user", "content": message}]
    else:
        llama_history.append({"role": "user", "content": message})
        
    chat_history.append({"role": "user", "content": message})

    response = client.responses.create(
        messages=llama_history,
        model="llama-3.1-8b-instant",
    )

    chat_history.append({"role": "assistant", "content": response.output_text})

    llama_history += response.output

    return "", chat_history
