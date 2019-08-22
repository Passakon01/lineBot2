from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นายภาสกร ศรีภุมมา เลขที่ 3 ชั้น ม.4/7"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    userText = decoded["events"][0]['message']['text']
    if (userText == "สวัสดี') :
        sendText(user,'ดีด้วยจ้าาา')
    elif (userText == 'สบายดีไหม') :
        sendText(user,'ยังไม่ตายค่ะ')
    else :
        sendText(user,'ว่าอะไรค่ะ.)
    return '',200
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
