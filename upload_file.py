from google import genai
import os
import time

# File Search 用クライアント
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# 作成済みのストアID
STORE_ID = "fileSearchStores/zetcwx20oo6y-e6zg8karixpr"

# アップロードするファイル
FILE_PATH = "attached_assets/shuugyouu_1763021286459.pdf"

print(f"ファイル '{FILE_PATH}' をストアにアップロード中...")

# ファイルをストアに直接アップロード
operation = client.file_search_stores.upload_to_file_search_store(
    file=FILE_PATH,
    file_search_store_name=STORE_ID,
    config={
        'display_name': '就業規則.pdf',
    }
)

print("アップロード処理を開始しました。完了を待っています...")

# インポート完了まで待機
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)
    print(".", end="", flush=True)

print("\n=== アップロード完了！ ===")
print(f"ファイルがストア '{STORE_ID}' に追加されました")
