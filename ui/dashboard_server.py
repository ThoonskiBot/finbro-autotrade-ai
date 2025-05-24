
from flask import Flask, render_template, request, redirect, jsonify
import json, os

app = Flask(__name__, template_folder='templates', static_folder='static')
CONFIG_PATH = "C:/FINBRO/config/strategy_states.json"
GPT_SUMMARY = "C:/FINBRO/reports/gpt_summary.txt"
PNL_COMMENT = "C:/FINBRO/reports/gpt_pnl_summary.txt"
SIGNAL_LOG = "C:/FINBRO/logs/signal_log.txt"

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/status")
def status():
    try:
        with open(CONFIG_PATH, "r") as f:
            strategies = json.load(f)
    except:
        strategies = {}
    try:
        with open(GPT_SUMMARY, "r", encoding="utf-8") as f:
            gpt = f.read()
    except:
        gpt = "No GPT summary available."
    try:
        with open(PNL_COMMENT, "r", encoding="utf-8") as f:
            pnl_summary = f.read()
    except:
        pnl_summary = "No PnL summary available."
    try:
        with open(SIGNAL_LOG, "r", encoding="utf-8") as f:
            signals = f.readlines()[-10:]
    except:
        signals = []
    return jsonify({"strategies": strategies, "gpt": gpt, "pnl_summary": pnl_summary, "signals": [s.strip() for s in signals]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
