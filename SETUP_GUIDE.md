# Gmail API OAuth 2.0 認証セットアップ

## ステップ1：Google Cloud Console設定

### 1-1. プロジェクト作成
1. https://console.cloud.google.com へアクセス
2. 上部の「プロジェクトを選択」をクリック
3. 「新規プロジェクト」をクリック
4. プロジェクト名を入力（例：`Gmail Auto Send`）
5. 「作成」をクリック

### 1-2. Gmail APIを有効化
1. Google Cloud Consoleで「APIとサービス」 → 「ライブラリ」をクリック
2. 検索欄に「Gmail」と入力
3. 「Gmail API」をクリック
4. 「有効にする」をクリック

### 1-3. OAuth 2.0認証情報を作成
1. 「APIとサービス」 → 「認証情報」をクリック
2. 「+ 認証情報を作成」 → 「OAuth クライアントID」をクリック
3. 「アプリケーションの種類」で「デスクトップアプリ」を選択
4. 名前を入力（例：`Gmail Auto Send App`）
5. 「作成」をクリック

### 1-4. JSON ファイルをダウンロード
1. 作成した認証情報の右側の「ダウンロードアイコン」をクリック
2. JSONファイルをダウンロード
3. このファイルを `credentials.json` という名前で、このフォルダに保存

## ステップ2：Pythonスクリプト実行

```bash
# 必要なライブラリをインストール
pip install google-auth-httplib2 google-auth-oauthlib google-api-python-client

# スクリプトを実行
python auto_send_email.py
```

初回実行時にブラウザが開きます。Googleアカウントで承認してください。

---

準備ができたら教えてください！
