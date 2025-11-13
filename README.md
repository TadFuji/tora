# 🏢 虎ノ門堂の規則 - 就業規則RAGチャットボット

Google Gemini の File Search 機能を使用した、就業規則に関する質問応答Webチャットボットです。
PDFファイルから情報を自動抽出し、ユーザーの質問に対してAIが正確な回答を生成します。

## ✨ 機能

- **RAG (Retrieval Augmented Generation)**: PDFから関連情報を自動抽出して回答を生成
- **引用元表示**: 回答の根拠となるPDF箇所を小さなボタンで表示、クリックで詳細確認
- **セキュアな設計**: XSS対策、エラー情報の隠蔽
- **モダンUI**: 紫グラデーションのチャットインターフェース

## 🚀 セットアップ

### 1. 必要な環境

- Python 3.11以上
- Google API Key (Gemini API)

### 2. インストール

```bash
# リポジトリをクローン
git clone https://github.com/your-username/toranomondo-rules.git
cd toranomondo-rules

# 依存パッケージをインストール
pip install -r requirements.txt
```

### 3. 環境変数の設定

`.env` ファイルを作成し、以下の環境変数を設定します：

```bash
GOOGLE_API_KEY=your_google_api_key_here
SESSION_SECRET=your_random_session_secret_here
```

Google API Key の取得方法：
1. [Google AI Studio](https://aistudio.google.com/app/apikey) にアクセス
2. API キーを作成
3. `.env` ファイルに貼り付け

### 4. File Search ストアのセットアップ

```bash
# File Search ストアを作成
python setup_store.py

# PDFファイルをアップロード
python upload_file.py
```

`setup_store.py` を実行すると、ストアIDが出力されます。
このIDを `app.py` の `STORE_ID` 変数に設定してください。

### 5. アプリケーションの起動

```bash
python app.py
```

ブラウザで http://localhost:5000 にアクセスしてください。

## 📖 使い方

1. チャット画面が開いたら、就業規則に関する質問を入力します
   - 例: 「試用期間について教えてください」
   - 例: 「有給休暇は何日ありますか？」
   
2. AIが回答を生成します

3. 回答の下部に「📚 参照元」として引用元が小さなボタン形式で表示されます

4. 📄 引用 1、📄 引用 2... のボタンをクリックすると、PDFからの引用テキストが確認できます

## 🛠 技術スタック

- **Frontend**: HTML/CSS/JavaScript
- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 2.5 Flash with File Search
- **RAG**: Google Gemini File Search (fully managed)

## 📁 プロジェクト構造

```
.
├── app.py                  # Flask Webアプリケーション
├── templates/
│   └── index.html         # チャットボットUI
├── setup_store.py         # File Search ストア作成スクリプト
├── upload_file.py         # PDFアップロードスクリプト
├── ask_question.py        # CLI質問スクリプト（オプション）
├── attached_assets/
│   └── *.pdf             # 就業規則PDFファイル
├── requirements.txt       # Python依存パッケージ
└── README.md             # このファイル
```

## 🔒 セキュリティ

- **XSS対策**: `textContent` を使用した安全なテキストレンダリング
- **エラー情報保護**: 一般的なエラーメッセージのみをクライアントに返し、詳細はサーバーログに記録
- **環境変数管理**: API キーやシークレットは環境変数で管理

## 📝 カスタマイズ

### PDFファイルの変更

1. `attached_assets/` に新しいPDFファイルを配置
2. `upload_file.py` のファイルパスを更新
3. `python upload_file.py` を実行してアップロード

### タイトルやデザインの変更

`templates/index.html` を編集してください。

## 🔧 トラブルシューティング

### 引用元が表示されない

- Gemini 2.5 Flash モデルを使用していることを確認してください
- Gemini 2.5 Flash-Lite は File Search をサポートしていません

### API エラーが発生する

- Google API Key が正しく設定されているか確認
- API キーの使用制限に達していないか確認
- [Google AI Studio](https://aistudio.google.com/) で API の状態を確認

## 📄 ライセンス

MIT License

## 🙏 謝辞

このプロジェクトは Google Gemini の File Search 機能を使用しています。
