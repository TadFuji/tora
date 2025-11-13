from google import genai
from google.genai import types
import os

# File Search 用クライアント
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# 作成済みのストアID
STORE_ID = "fileSearchStores/zetcwx20oo6y-e6zg8karixpr"

# 質問内容（ここを変更して様々な質問ができます）
question = "試用期間について教えてください"

print(f"質問: {question}\n")
print("回答を生成中...\n")

# File Search を使って質問に回答
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[STORE_ID]
                )
            )
        ]
    )
)

print("=" * 60)
print("【回答】")
print("=" * 60)
print(response.text)
print("=" * 60)

# 引用情報があれば表示
if hasattr(response, 'candidates') and response.candidates:
    candidate = response.candidates[0]
    if hasattr(candidate, 'grounding_metadata'):
        print("\n【参照元】")
        print("File Search により就業規則から情報を取得しました")
