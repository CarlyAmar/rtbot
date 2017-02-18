import os
from flask import Flask, request, Response

import requests
import json

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get("SLACK_WEBHOOK_SECRET")
WEBHOOK_URL=os.environ.get("WEBHOOK_URL")


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
        slack_data={"text":"@ksarkhel RT: \""+text+"\""}
        if username == "ksarkhel":
            requests.post(WEBHOOK_URL, data=json.dumps(slack_data), headers={"Content-type":"application/json"})
    return Response()


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
