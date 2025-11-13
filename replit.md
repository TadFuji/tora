# 就業規則RAGシステム - 虎ノ門堂の規則

## Overview
Google Gemini の File Search 機能を使用した、就業規則に関する質問応答Webチャットボットです。
PDFファイルから情報を抽出し、ユーザーの質問に対してAIが正確な回答を生成します。
回答の下部にはPDFからの引用元が小さなボタン形式で表示され、クリックすると詳細を確認できます。

## Recent Changes
- **引用元のボタン形式UI** (November 13, 2025)
  - 引用元を小さなボタン（📄 引用 1、📄 引用 2...）形式に変更
  - クリックで詳細テキストが展開/折りたたみ
  - より省スペースでコンパクトな表示
- **引用元表示機能の追加** (November 13, 2025)
  - grounding_metadataから引用元情報を抽出
  - 回答の下部に「📚 参照元」として表示
  - PDFからの抜粋テキストを表示してRAGの動作を可視化
- **Flask Webアプリケーション完成** (November 13, 2025)
  - モダンな紫グラデーションのチャットUIを実装
  - セキュリティ脆弱性（XSS、エラー情報漏洩）を修正
  - textContentを使用した安全なテキストレンダリング
  - 一般的なエラーメッセージでサーバー詳細を隠蔽
- 就業規則PDFファイルのアップロード完了 (November 13, 2025)
- ask_question.py 動作確認完了 (November 13, 2025)
- File Search store created: fileSearchStores/zetcwx20oo6y-e6zg8karixpr (November 13, 2025)
- google-genai package installed (November 13, 2025)
- GOOGLE_API_KEY stored in environment secrets (November 13, 2025)
- Initial project setup (November 13, 2025)

## Project Structure
### Web Application
- `app.py` - Flask Webアプリケーション（ポート5000）
  - grounding_metadata から引用元情報を抽出
  - /chat エンドポイントでreplyとsourcesを返す
- `templates/index.html` - チャットボットUI（紫グラデーション、モダンデザイン）
  - 引用元を小さなボタン形式で表示
  - クリックで詳細テキストを展開/折りたたみ
  - 「📚 参照元」セクションで引用元を可視化

### Setup Scripts
- `setup_store.py` - File Search storeを作成するスクリプト
- `upload_file.py` - PDFファイルをストアにアップロードするスクリプト
- `ask_question.py` - CLIで就業規則に関する質問を行うスクリプト

### Assets
- `attached_assets/shuugyouu_1763021286459.pdf` - 就業規則PDF（アップロード済み）

## Dependencies
- `flask` - Webフレームワーク
- `flask-cors` - CORS対応
- `google-genai` (v1.50.0) - Google Generative AI SDK for Python
- `google-generativeai` - Google Generative AI SDK (legacy, for compatibility)

## File Search Store
- Store Name: 就業規則ストア
- Store ID: `fileSearchStores/zetcwx20oo6y-e6zg8karixpr`
- Created: November 13, 2025
- Uploaded Files: 就業規則.pdf
- Model: gemini-2.5-flash

## Usage
### Web Application
Webアプリケーションはポート5000で自動起動します：
- URLにアクセスしてチャットボットを使用
- タイトル：「🏢 虎ノ門堂の規則」
- 質問例：「試用期間について教えてください」「有給休暇について知りたい」
- 回答の下部に「📚 参照元」が小さなボタン形式で表示されます
- ボタン（📄 引用 1、📄 引用 2...）をクリックすると、PDFからの引用テキストが表示されます

### CLI (Optional)
質問スクリプトを実行：
```bash
python ask_question.py
```

## Secrets
- `GOOGLE_API_KEY` - Google API Key stored securely in environment variables
  - Access in code: `os.environ.get('GOOGLE_API_KEY')`
- `SESSION_SECRET` - Flask session secret

## Security Features
- XSS防止: textContentを使用した安全なテキストレンダリング
- エラー情報保護: 一般的なエラーメッセージのみをクライアントに返す
- サーバーサイドログ: 詳細なエラーはサーバーログにのみ記録

## Features
- **RAG (Retrieval Augmented Generation)**: PDFから関連情報を自動抽出
- **引用元表示（ボタン形式）**: 回答の根拠となるPDF箇所を小さなボタンで表示、クリックで詳細確認
- **セキュアな設計**: XSS対策、エラー情報の隠蔽
- **モダンUI**: 紫グラデーションのチャットインターフェース

## User Preferences
- タイトル: 「虎ノ門堂の規則」を使用
- デザイン: 紫グラデーションのモダンなチャットUI
- 引用元表示: 小さなボタン形式で省スペース、クリックで詳細展開

## Project Architecture
Google Gemini の File Search 機能を使用したRAG（Retrieval Augmented Generation）システム。
Flask Webアプリケーションとして実装し、PDFファイルから自動的に情報を抽出して質問に対して正確な回答を生成します。

### Architecture Details
- Frontend: HTML/CSS/JavaScript（シングルページチャットUI）
- Backend: Flask REST API（/chat エンドポイント）
- AI Model: Google Gemini 2.5 Flash with File Search
- Security: textContent rendering, generic error messages
- RAG Visualization: grounding_metadata から引用元を抽出し、小さなボタン形式で表示
