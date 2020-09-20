from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from postgresql import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import psycopg2
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('tG2+BvqixjrHDIX6jhmCcW+g5LMa4fumy+Zm6PdnyFJleHpK0F1pn4KGeRV7NCvZsqU40mmi1NJsvgq5Ozq2MdZHxV6l8wT/Kp0CGkfApeUhHSFwWMRWHsOBepB/p0jTlCZrfECMhlTaO0lQ3umGlgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('4028d87a97d982c2049e4a0ad2131698')

# Test database class
db = postgre()

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    msg = event.message.text
    user_id = event.source.user_id
    if db.new_user(user_id):
        print(user_id, 'is a new user')
        db.user_registration(user_id, "0", "university", "department", "studentid", 100, "name", "student_id_card", "line_id")
    else:
        print(user_id, 'has already registered')
        
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

