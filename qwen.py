from openai import OpenAI
import gradio as gr
import time

def qwen(message, chat_history, key):
    global qwen_history
    if not key:
        gr.Warning("Qwen: API Keyを入力してください。")
        time.sleep(1)
        return "", chat_history
        
    if not message:
        gr.Warning("Qwen: プロンプトを入力してください。")
        time.sleep(1)
        return "", chat_history
    
    with open('groq_api_key.txt', 'w') as f:
        f.write(key) 

    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1",
    )

    if not chat_history:
        qwen_history = [{"role": "user", "content": message}]
    else:
        qwen_history.append({"role": "user", "content": message})
        
    chat_history.append({"role": "user", "content": message})

    response = client.responses.create(
        input=qwen_history,
        model="qwen/qwen3.8-27b",
    )

    chat_history.append({"role": "assistant", "content": response.output_text})

    qwen_history += response.output

    return "", chat_history
