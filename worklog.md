# 🏢 虎ノ門堂の規則 - 就業規則RAGチャットボット開発レポート

## 📋 プロジェクト概要
Google Gemini の File Search 機能を使用した、就業規則に関する質問応答Webチャットボットの開発

---

## 📅 作業履歴（時系列）

### **Phase 1: 初期セットアップ（2025年11月13日 午前）**

#### ✅ 実施内容
1. **Google Gemini API の環境構築**
   - `GOOGLE_API_KEY` を環境変数として設定
   - `google-genai` パッケージ（v1.50.0）をインストール
   - `google-generativeai` パッケージもインストール（互換性のため）

2. **File Search ストアの作成**
   - `setup_store.py` スクリプトを作成
   - ストア名: 「就業規則ストア」
   - ストアID: `fileSearchStores/zetcwx20oo6y-e6zg8karixpr`
   - 正常に作成完了

3. **PDFファイルのアップロード**
   - `upload_file.py` スクリプトを作成
   - 就業規則PDF（`attached_assets/shuugyouu_1763021286459.pdf`）をアップロード
   - File Search ストアに正常に登録完了

4. **CLI動作確認**
   - `ask_question.py` スクリプトを作成
   - コマンドラインで質問機能をテスト
   - RAG機能が正常に動作することを確認

---

### **Phase 2: Webアプリケーション開発（午前〜午後）**

#### ✅ 実施内容

1. **Flask Webアプリケーションの基礎構築**
   - `app.py` を作成（ポート5000で起動）
   - `/` エンドポイント: チャット画面表示
   - `/chat` エンドポイント: 質問処理API
   - Flask-CORS を導入してCORS対応

2. **チャットUIの実装**
   - `templates/index.html` を作成
   - デザイン要件:
     - タイトル: 「🏢 虎ノ門堂の規則」
     - 紫グラデーション背景（`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`）
     - モダンなチャットインターフェース
     - 送信ボタン: 「送信」ラベル

3. **セキュリティ対策の実装**
   - **XSS（クロスサイトスクリプティング）対策**
     - 当初: `innerHTML` を使用（脆弱性あり）
     - 修正: `textContent` を使用した安全なテキストレンダリング
   
   - **エラー情報の保護**
     - サーバーエラーの詳細をクライアントに送信しない
     - 一般的なエラーメッセージのみを返す
     - 詳細なエラーはサーバーログにのみ記録

---

### **Phase 3: 引用元表示機能の実装（午後）**

#### ✅ 実施内容

1. **grounding_metadata からの引用元抽出**
   - Gemini レスポンスの `grounding_metadata` を解析
   - 各引用元から以下を抽出:
     - `retrieval_queries`: 検索クエリ
     - `grounding_chunks`: 引用テキスト（最大200文字）
   - `/chat` エンドポイントで `sources` 配列を返すように実装

2. **UI実装の変遷**
   
   **第1版: 大きなボックス形式**
   - 引用元を回答の下に大きなボックスとして表示
   - 各引用元がかなりのスペースを占有
   
   **問題点:**
   - ユーザーから「小さなボタン形式にしてほしい」との要望
   
   **第2版: 小さなボタン形式（最終版）**
   - 「📚 参照元」セクションを追加
   - 各引用元を小さなボタンで表示（例: 📄 引用 1、📄 引用 2）
   - クリックで詳細テキストが展開/折りたたみ
   - CSS で省スペース化、ホバー効果も追加

3. **UIの細かい調整**
   - 初期メッセージの空白処理問題を修正
   - `white-space: pre-wrap` を適切に適用
   - ボタンのスタイリング調整（パディング、角丸、影）

---

### **Phase 4: モデルの問題と解決（午後〜夕方）**

#### ❌ 問題発生

**Gemini 2.5 Flash-Lite への変更試行**
- 高速化とコスト削減を目的に Flash-Lite への変更を検討
- `app.py` のモデル名を `gemini-2.5-flash-lite` に変更
- ワークフローを再起動

**症状:**
```
✅ 回答: 試用期間は原則として3ヶ月です...
❌ 引用元数: 0  ← 引用元が空！
```

#### 🔍 原因調査

1. **Web検索を実施**
   - クエリ: "gemini 2.5 flash lite file search support"
   
2. **判明した事実**
   - ✅ **Gemini 2.5 Flash**: File Search サポート
   - ✅ **Gemini 2.5 Pro**: File Search サポート
   - ❌ **Gemini 2.5 Flash-Lite**: **File Search 非サポート**

3. **Flash-Lite の特性**
   - 速度とコスト効率を重視した軽量モデル
   - 用途: 分類、翻訳、シンプルな質問応答
   - サポート機能:
     - ✅ Google Search grounding（別機能）
     - ✅ Code execution
     - ✅ 1M トークンコンテキスト
     - ❌ **File Search（RAG機能）**

#### ✅ 解決方法

1. **モデルを元に戻す**
   ```python
   # 修正前（動作しない）
   model="gemini-2.5-flash-lite"
   
   # 修正後（正常動作）
   model="gemini-2.5-flash"
   ```

2. **動作確認**
   ```bash
   curl テスト実施
   ✅ 回答: 試用期間は原則として3ヶ月です...
   ✅ 引用元数: 4  ← 正常に動作！
   ```

3. **ドキュメント更新**
   - `replit.md` の Model 情報を修正
   - `gemini-2.5-flash-lite` → `gemini-2.5-flash`

**教訓:**
- RAG（Retrieval Augmented Generation）機能が必要な場合は、必ず Flash または Pro を使用
- Flash-Lite は RAG 非対応のため、File Search を使うプロジェクトでは使用不可

---

### **Phase 5: GitHub準備（夕方）**

#### ✅ 実施内容

1. **.gitignore の作成**
   ```gitignore
   # Python関連
   __pycache__/, *.pyc, *.pyo
   
   # 環境変数（重要！）
   .env, .env.local
   
   # Replit固有ファイル
   .replit, replit.nix, uv.lock, replit.md, main.py
   
   # プロジェクト固有
   static/, /tmp/, attached_assets/image_*.png
   ```
   
   **ポイント:**
   - `.env` を除外してAPI キーを保護
   - Replit固有ファイルを除外
   - 一時ファイルやログを除外

2. **README.md の作成**
   - プロジェクト概要
   - 機能説明
   - セットアップ手順（詳細）
   - 使い方
   - トラブルシューティング
     - **特記事項:** Flash-Lite は File Search 非対応と明記
   - 技術スタック
   - セキュリティ機能

3. **requirements.txt の作成**
   ```txt
   flask>=3.1.2
   flask-cors>=6.0.1
   google-genai>=1.50.0
   google-generativeai>=0.8.5
   gunicorn
   ```

4. **不要ファイルの削除**
   - `main.py` 削除（Replitのテストファイル）
   - `static/` ディレクトリ削除（空だった）
   - `attached_assets/image_*.png` 削除（スクリーンショット）

---

### **Phase 6: デプロイ設定（夕方）**

#### ✅ 実施内容

1. **Gunicorn のインストール**
   - 本番環境用WSGIサーバー
   - `packager_tool` で `gunicorn` をインストール
   - `requirements.txt` に追加

2. **デプロイ設定**
   - デプロイタイプ: **Autoscale**
     - ステートレスWebアプリケーション向け
     - リクエストがある時のみ起動
     - 自動スケーリング対応
   
   - 実行コマンド:
     ```bash
     gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
     ```

3. **ワークフロー設定**
   - 名前: `web`
   - コマンド: Gunicorn起動コマンド
   - ポート: 5000（webview）
   - 出力タイプ: `webview`

4. **最終動作確認**
   - Gunicorn での起動確認: ✅
   - RAG機能の動作確認: ✅（引用元5個抽出）
   - UI表示確認: ✅
   - セキュリティ確認: ✅

---

## 🎯 完成した機能

### ✅ 主要機能
1. **RAG（Retrieval Augmented Generation）**
   - Google Gemini 2.5 Flash + File Search
   - PDFから自動的に関連情報を抽出
   - 正確な回答生成

2. **引用元表示（小さなボタン形式）**
   - 回答の根拠となるPDF箇所を可視化
   - クリックで詳細テキストを展開/折りたたみ
   - 省スペースでコンパクトなUI

3. **セキュリティ**
   - XSS対策（`textContent` 使用）
   - エラー情報の隠蔽
   - 環境変数による機密情報管理

4. **モダンUI**
   - 紫グラデーション背景
   - レスポンシブデザイン
   - スムーズなアニメーション

---

## ⚠️ 遭遇した問題と解決策

### 問題1: Gemini 2.5 Flash-Lite で File Search が動作しない

**問題:**
- Flash-Lite に変更したら引用元が0件になった
- RAG機能が完全に動作しない

**原因:**
- Gemini 2.5 Flash-Lite は File Search 機能をサポートしていない
- Flash-Lite は軽量タスク（分類、翻訳）向け

**解決:**
- Gemini 2.5 Flash に戻す
- ドキュメントに注意事項を追加

### 問題2: XSSセキュリティ脆弱性

**問題:**
- `innerHTML` を使用していたためXSS攻撃のリスク

**解決:**
- `textContent` を使用した安全なレンダリングに変更
- ユーザー入力を適切にエスケープ

### 問題3: 引用元UIが大きすぎる

**問題:**
- 最初の実装では引用元が大きなボックスで表示
- 画面を圧迫

**解決:**
- 小さなボタン形式に変更
- クリックで展開する折りたたみ式UI

---

## 📊 最終的なファイル構造

```
.
├── app.py                  # Flask Webアプリケーション
├── templates/
│   └── index.html         # チャットボットUI
├── attached_assets/
│   └── *.pdf             # 就業規則PDF
├── setup_store.py         # File Search ストア作成
├── upload_file.py         # PDFアップロード
├── ask_question.py        # CLI質問ツール
├── README.md             # プロジェクトドキュメント
├── requirements.txt      # Python依存パッケージ
├── .gitignore           # Git除外設定
└── pyproject.toml       # プロジェクト設定
```

---

## 🚀 デプロイ準備完了

### 設定内容
- **サーバー:** Gunicorn (本番用WSGI)
- **デプロイタイプ:** Autoscale（ステートレス、自動スケーリング）
- **ポート:** 5000
- **環境変数:** `GOOGLE_API_KEY`, `SESSION_SECRET`

### 次のステップ
1. Replitの「Publish」ボタンをクリック
2. 環境変数が自動的に引き継がれる
3. 公開URLが発行される
4. 世界中からアクセス可能に

---

## 📚 学んだこと

1. **Gemini モデルの選択は重要**
   - RAG機能が必要 → Flash または Pro
   - 軽量タスクのみ → Flash-Lite でコスト削減可能

2. **セキュリティは最初から組み込む**
   - XSS対策、エラー情報の隠蔽は必須
   - 環境変数で機密情報を管理

3. **UIは反復改善**
   - 最初の実装からユーザーフィードバックで改善
   - 小さなボタン形式の方が実用的

4. **本番環境は開発環境と別**
   - Flask開発サーバー → Gunicorn
   - Autoscaleでコスト最適化
