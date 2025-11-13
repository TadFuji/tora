import google.generativeai as genai
import os

# APIキーをロード
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# File Search 用クライアント
client = genai.Client()

# ストアにつける名前（自由）
STORE_DISPLAY_NAME = "就業規則ストア"

print(f"'{STORE_DISPLAY_NAME}' を作成します...")

# ストア作成
file_search_store = client.file_search_stores.create(
    config={'display_name': STORE_DISPLAY_NAME}
)

print("=== 作成完了！ ===")
print("この Store ID をメモしてください ↓")
print(file_search_store.name)
