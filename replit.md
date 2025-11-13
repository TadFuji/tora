# 就業規則RAGシステム

## Overview
Google Gemini の File Search 機能を使用した、就業規則に関する質問応答システムです。
PDFファイルをアップロードし、AIが内容を理解して正確な回答を生成します。

## Recent Changes
- 就業規則PDFファイルのアップロード完了 (November 13, 2025)
- ask_question.py 動作確認完了 (November 13, 2025)
- File Search store created: fileSearchStores/zetcwx20oo6y-e6zg8karixpr (November 13, 2025)
- google-generativeai package installed (November 13, 2025)
- google-genai package installed (November 13, 2025)
- GOOGLE_API_KEY stored in environment secrets (November 13, 2025)
- Initial project setup (November 13, 2025)
- Python 3.11 environment configured

## Project Structure
- `main.py` - Main entry point for the Python application
- `setup_store.py` - File Search storeを作成するスクリプト
- `upload_file.py` - PDFファイルをストアにアップロードするスクリプト
- `ask_question.py` - 就業規則に関する質問を行うスクリプト
- `attached_assets/shuugyouu_1763021286459.pdf` - 就業規則PDF（アップロード済み）

## Dependencies
- `google-genai` (v1.50.0) - Google Generative AI SDK for Python
- `google-generativeai` - Google Generative AI SDK (legacy, for compatibility)

## File Search Store
- Store Name: 就業規則ストア
- Store ID: `fileSearchStores/zetcwx20oo6y-e6zg8karixpr`
- Created: November 13, 2025
- Uploaded Files: 就業規則.pdf

## Usage
質問スクリプトを実行：
```bash
python ask_question.py
```

質問内容を変更する場合は、`ask_question.py` の `question` 変数を編集してください。

## Secrets
- `GOOGLE_API_KEY` - Google API Key stored securely in environment variables
  - Access in code: `os.environ.get('GOOGLE_API_KEY')`

## User Preferences
None specified yet.

## Project Architecture
Google Gemini の File Search 機能を使用したRAG（Retrieval Augmented Generation）システム。
PDFファイルから自動的に情報を抽出し、質問に対して正確な回答を生成します。
