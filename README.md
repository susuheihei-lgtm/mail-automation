# Gmail 自動送信機能

OAuth 2.0認証を使用した、Gmail メール自動送信スクリプトです。

## 📋 準備手順

### 1. Google Cloud Console設定

`SETUP_GUIDE.md` の手順に従って、`credentials.json` を取得・保存してください。

### 2. ライブラリインストール

```bash
pip install -r requirements.txt
```

または個別に：

```bash
pip install google-auth-httplib2 google-auth-oauthlib google-api-python-client
```

## 🚀 実行方法

### 初回実行

```bash
python auto_send_email.py
```

ブラウザが開きます。Googleアカウントで認可してください。

### 2回目以降

```bash
python auto_send_email.py
```

自動でメールが送信されます。

## 📧 メール内容のカスタマイズ

`auto_send_email.py` の以下の部分を編集：

```python
TO_ADDRESS = "送信先メールアドレス"
SUBJECT = "件名"
BODY_HTML = """
メール本文（HTML形式）
"""
```

## ⏰ 定期実行（毎日実行例）

### Mac/Linux

```bash
# crontabエディタを開く
crontab -e

# 毎日9時に実行
0 9 * * * /Users/iwasaosamutaira/Desktop/マイデジタルプロダクト/自動化/run_email.sh
```

### Windows

Windowsタスクスケジューラで設定してください。

## 📝 ファイル構成

- `auto_send_email.py` - メール送信メインスクリプト
- `run_email.sh` - 実行用シェルスクリプト
- `requirements.txt` - 必要なPythonライブラリ
- `SETUP_GUIDE.md` - Google Cloud Console設定ガイド
- `credentials.json` - OAuth認証情報（自分で取得）
- `token.pickle` - 認証トークン（初回実行時に自動生成）

## ⚠️ セキュリティ注意

- `credentials.json` と `token.pickle` を他人と共有しないこと
- `.gitignore` に追加して、バージョン管理から除外すること

## ✅ トラブルシューティング

- ブラウザが開かない → ターミナルに表示されたURLを手動で開く
- "Permission denied" → `run_email.sh` に実行権限を付与: `chmod +x run_email.sh`
