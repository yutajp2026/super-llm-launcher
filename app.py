import os
import time
import platform
import webbrowser
import gradio as gr
import gemini
import chatgpt
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
        message = gr.Textbox(label="Prompt", placeholder="Geminiに相談")
        api_key = gr.Textbox(label="API Key", value=gemini_api_key if os.path.exists('gemini_api_key.txt') else "", type="password")
        message.submit(gemini.gemini, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("ChatGPT"):
        gr.Markdown("# ChatGPT 6 Luna")
        gr.Markdown("どこから始めますか？")
        gr.Markdown("API keyを[ここ](https://platform.openai.com/api-keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox(label="Prompt", placeholder="ChatGPTに聞く")
        api_key = gr.Textbox(label="API Key", value=gpt_api_key if os.path.exists('gpt_api_key.txt') else "", type="password")
        message.submit(chatgpt.gpt, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("Qwen"):
        gr.Markdown("# Qwen 3.8")
        gr.Markdown("クウェンに聞いてみて、もっと知りたい。")
        gr.Markdown("API keyを[ここ](https://console.groq.com/keys)から取得して、会話を始めましょう。")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox(label="Prompt", placeholder="今日はどのようにお手伝いできますか？")
        api_key = gr.Textbox(label="API Key", value=groq_api_key if os.path.exists('groq_api_key.txt') else "", type="password")
        message.submit(qwen.qwen, [message, chatbot, api_key], [message, chatbot])
    with gr.Tab("メニュー"):
        gr.Markdown("# サーバー")
        def quit(save_keys: bool):
            if not save_keys:
                if os.path.exists('gemini_api_key.txt'):
                    os.remove('gemini_api_key.txt')
                if os.path.exists('gpt_api_key.txt'):
                    os.remove('gpt_api_key.txt')
                if os.path.exists('groq_api_key.txt'):
                    os.remove('groq_api_key.txt')
            gr.Info("アプリケーション終了。タブは手動で閉じてください。")
            time.sleep(1)
            os._exit(0)
        save_keys = gr.Checkbox(label="APIキーを保持", value=True, interactive=True)
        quit_btn = gr.Button("終了")
        quit_btn.click(fn=quit, inputs=[save_keys], outputs=[])
        gr.Markdown("# 製品について")
        gr.Markdown("https://github.com/yutajp2026/super-llm-launcher")
        version = os.getenv("VERSION")
        if version:
            gr.Markdown("最新のバージョンは、上記GitHubページで確認できます。")
            gr.Markdown("現在使用しているアプリのバージョン: " + version)
            

if platform.system() == "Windows":
    webbrowser.open('http://127.0.0.1:7860')
else:
    print("ブラウザで以下のURLを開いてください。")

demo.launch()