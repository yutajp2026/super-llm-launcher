# Super LLM Launcher

Super LLM Launcher は、複数の大規模言語モデルを1つのアプリから利用できるようにしたローカル向けランチャーです。

# 特徴

- 複数モデルの切り替え
  - 現時点ではGemini、ChatGPT、Qwenと会話できます。
  - 各モデルごとに専用タブを用意し、同時に複数のAIサービスを比較しながら使えます。

- シンプルなUI
  - Gradio をベースにした軽量なインターフェースを採用しています。
  - プロンプト入力欄とチャット履歴の表示が一目で確認できます。

- APIキー
  - 直前に入力したAPIキーは自動でローカルファイルに保存されます。
  - アプリ終了時にAPIキーを保持するかどうかを選択できます。

- 会話の継続
  - 各モデルの会話履歴が起動中は保持され、同じセッション内で自然な文脈でやり取りを続けられます。

- ブラウザ起動の簡略化
  - アプリ起動時にローカルのブラウザURLを自動で開くため、すぐに利用を開始できます(Windowsのみ)。

# インストール
## Windows
Releasesにインストーラを公開予定
## Linux
1. 下記のコマンドでPythonとgitをインストール
```bash
# Debian系(Ubuntuなど)
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```
```bash
# Red Hat系(Oracle Linuxなど)
sudo dnf install python3 python3-pip python3-venv git
```
```bash
# Arch系
sudo pacman install python3 python3-pip python3-venv git
```
```bash
# SUSE系
sudo zypper install python3 python3-pip python3-venv git
```
2. `git clone https://github.com/yutajp2026/super-llm-launcher.git`でこのリポジトリをクローン
3. `cd super-llm-launcher`でスクリプトディレクトリに移動
4. `bash launcher.sh`で実行 ⚠️linuxの場合は自動でブラウザを開きません。
5. `git pull`でアップデート

# ライセンス

本プロジェクトは、必要に応じて自由に改変・利用できます。ただし、悪用は厳禁です。なお、改変時は各AIのライセンスを守ってください。
