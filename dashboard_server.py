
from flask import Flask, render_template, jsonify, request
import os, json
from dashboard_utils import get_active_strategies, get_pnl
from pnl_log_reader import read_pnl_from_logs

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logs")
def logs():
    try:
        with open("logs/order_log_test_2025-05-26.txt", "r") as f:
            return f.read(), 200
    except:
        return "Log file not found.", 404

@app.route("/summary")
def summary():
    try:
        latest_file = sorted(
            [f for f in os.listdir("reports") if f.startswith("gpt_trade_summary_") and f.endswith(".txt")],
            reverse=True
        )[0]
        with open(f"reports/{latest_file}", "r") as f:
            return f.read(), 200
    except:
        return "Summary not available.", 404

@app.route("/pnl")
def pnl():
    return jsonify(get_pnl())

@app.route("/strategies", methods=["GET", "POST"])
def strategies():
    config_path = "C:/FINBRO/strategy_config.json"
    if request.method == "POST":
        data = request.get_json()
        with open(config_path, "w") as f:
            json.dump(data, f)
        return jsonify({"status": "saved"})
    else:
        try:
            with open(config_path, "r") as f:
                return jsonify(json.load(f))
        except:
            return jsonify({s: True for s in ["momentum", "reversal", "neutral"]})

@app.route("/pnl_data")
def pnl_data():
    return jsonify(read_pnl_from_logs("C:/FINBRO/logs"))

if __name__ == "__main__":
    app.run(debug=True)
