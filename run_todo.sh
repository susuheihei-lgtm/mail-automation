#!/bin/bash
cd /Users/iwasaosamutaira/Desktop/マイデジタルプロダクト/自動化
source venv/bin/activate
python auto_send_todo_list.py >> email_send.log 2>&1
