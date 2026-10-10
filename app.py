import os
import time
import platform
import webbrowser
import gradio as gr
import gemini
import chatgpt
import llama
import qwen

if os.path.exists('gemini_api_key.txt'):
    with open('gemini_api_key.txt', "r", encoding="utf-8") as f:
        gemini_api_key = f.read()

if os.path.exists('gpt_api_key.txt'):
    with open('gpt_api_key.txt', "r", encoding="utf-8") as f:
        gpt_api_key = f.read()

if os.path.exists('groq_api_key.txt'):
    with open('groq_api_key.txt', "r", encoding="utf-8") as f:
        groq_api_key = f.read()

with gr.Blocks() as demo:
    with gr.Tab("Gemini"):
        gr.Markdown("# Gemini 3.5 Flash")
        gr.Markdown("何かお手伝いできることはありますか？")
        gr.Markdown("API keyを[ここ](https://aistudio.google.com/api-keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder="Geminiに相談")
        api_key = gr.Textbox(label="API Key", value=gemini_api_key if os.path.exists('gemini_api_key.txt') else "", type="password")
        message.submit(gemini.gemini, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("ChatGPT"):
        gr.Markdown("# ChatGPT 6 Luna")
        gr.Markdown("どこから始めますか？")
        gr.Markdown("API keyを[ここ](https://platform.openai.com/api-keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder="ChatGPTに聞く")
        api_key = gr.Textbox(label="API Key", value=gpt_api_key if os.path.exists('gpt_api_key.txt') else "", type="password")
        message.submit(chatgpt.gpt, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("Llama"):
        gr.Markdown("# Llama 3.1 Instant")
        gr.Markdown("API keyを[ここ](https://console.groq.com/keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox()
        api_key = gr.Textbox(label="API Key", value=groq_api_key if os.path.exists('groq_api_key.txt') else "", type="password")
        message.submit(llama.llama, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("Qwen"):
        gr.Markdown("# Qwen 3.8")
        gr.Markdown("API keyを[ここ](https://console.groq.com/keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox()
        api_key = gr.Textbox(label="API Key", value=groq_api_key if os.path.exists('groq_api_key.txt') else "", type="password")
        message.submit(qwen.qwen, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("メニュー"):
        gr.Markdown("## サーバー")
        def quit():
            gr.Info("アプリケーション終了。タブは手動で閉じてください。")
            time.sleep(1)
            os._exit(0)
        quit_btn = gr.Button("終了")
        quit_btn.click(fn=quit, inputs=[], outputs=[])

if platform.system() == "Windows":
    webbrowser.open('http://127.0.0.1:7860')
else:
    print("ブラウザで以下のURLを開いてください。")

demo.launch()