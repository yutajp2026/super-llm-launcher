import webbrowser
import gradio as gr
import platform
import gemini
import os

if os.path.exists('gemini_api_key.txt'):
    with open('gemini_api_key.txt', "r", encoding="utf-8") as f:
        gemini_api_key = f.read()

with gr.Blocks() as demo:
    with gr.Tab("Gemini"):
        gr.Markdown("# Gemini 3.8 Flash")
        gr.Markdown("何かお手伝いできることはありますか？")
        gr.Markdown("※エラーはバックエンドウィンドウに表示されます。")
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder="Geminiに相談")
        api_key = gr.Textbox(label="API Key", value=gemini_api_key if os.path.exists('gemini_api_key.txt') else "", type="password")
        message.submit(gemini.gemini, [message, chatbot, api_key], [message, chatbot])
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