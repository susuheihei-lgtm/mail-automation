#!/bin/bash
# Gmail 自動送信スクリプト実行用シェルスクリプト

# スクリプトのディレクトリに移動
cd "$(dirname "$0")"

# Pythonスクリプトを実行
python3 auto_send_email.py

# 実行ログ
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Email send script executed" >> email_send.log
