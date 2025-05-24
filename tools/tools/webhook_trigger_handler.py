# Phase 93 – API/Webhook Triggers
from flask import Flask, request

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_action():
    data = request.json
    # Do something with the incoming data
    return {"status": "received", "data": data}, 200

def start_webhook_server():
    app.run(host="0.0.0.0", port=8080)