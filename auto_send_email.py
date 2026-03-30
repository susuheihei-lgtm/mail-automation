#!/usr/bin/env python3
"""
Gmail 自動送信スクリプト
OAuth 2.0 認証を使用して、メールを自動送信します
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

# Gmail APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    """OAuth 2.0 認証を実行"""
    creds = None

    # token.pickleがあれば前回の認証情報を使用
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # 認証情報がない、または期限切れの場合
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # credentials.jsonを使用して認証フロー開始
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # 認証情報を保存
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def send_email(to_address, subject, body_html, body_text=None):
    """
    メールを送信

    Args:
        to_address (str): 送信先メールアドレス
        subject (str): メール件名
        body_html (str): HTML形式のメール本文
        body_text (str): テキスト形式のメール本文（省略可）
    """
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    # テキスト版がない場合は、HTMLから自動生成
    if body_text is None:
        body_text = body_html.replace('<br>', '\n').replace('<p>', '').replace('</p>', '\n')

    # メール作成
    message = MIMEText(body_html, 'html')
    message['to'] = to_address
    message['subject'] = subject

    # Base64エンコード
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # 送信
    try:
        send_message = service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()

        print(f"✅ メール送信成功！")
        print(f"   宛先: {to_address}")
        print(f"   件名: {subject}")
        print(f"   Message ID: {send_message['id']}")
        return send_message

    except Exception as e:
        print(f"❌ エラー: {e}")
        return None

if __name__ == '__main__':
    # 設定例
    TO_ADDRESS = "e741022@wakayama-u.ac.jp"
    SUBJECT = "【ToDoリスト】日本マスタートラスト信託銀行 対応事項まとめ"

    BODY_HTML = """
    <html>
      <body>
        <p>お疲れ様です。</p>
        <p>本日のToDoリストをお送りします。</p>
        <br>
        <p>【対応事項】</p>
        <p>1. 日本マスタートラスト信託銀行との打ち合わせ準備</p>
        <p>2. 資料の確認と修正</p>
        <p>3. メール送信テスト</p>
        <br>
        <p>よろしくお願いいたします。</p>
      </body>
    </html>
    """

    send_email(TO_ADDRESS, SUBJECT, BODY_HTML)
