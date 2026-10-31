#!/bin/bash

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 が見つかりません。Python 3 をインストールしてください。" >&2
    exit 1
fi

echo "仮想環境を作成中..."
if [ ! -d ".venv" ]; then
    python3 -m venv ".venv"
fi

# shellcheck disable=SC1090
source ".venv/bin/activate"

echo "pip を更新中..."
python -m pip install --upgrade pip

echo "パッケージをインストール中..."
python -m pip install gradio google-genai openai

echo "アプリを起動中..."
python app.py
