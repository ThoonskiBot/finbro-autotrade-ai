from flask import Flask, render_template
import csv
import json
from datetime import date
from pathlib import Path
from alpaca_pnl_fetcher import get_alpaca_pnl

app = Flask(__name__, static_folder="../reports", static_url_path="/static")

@app.route('/')
def dashboard():
    # 🧠 Load GPT summary based on today's date
    gpt_file = None
    today = date.today().strftime("%Y-%m-%d")
    for path in Path("../reports").glob(f"gpt_trade_summary_{today}_*.txt"):
        gpt_file = path
        break
    gpt_summary = gpt_file.read_text() if gpt_file and gpt_file.exists() else "No GPT summary for today."

    # 📈 Load PnL CSV
    pnl_file = Path("../logs/pnl_by_date.csv")
    dates, pnl_values = [], []

    if pnl_file.exists():
        with open(pnl_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                dates.append(row["date"])
                pnl_values.append(float(row["pnl"]))

    # 📊 Chart data for Plotly
    chart_data = {
        "data": [
            {
                "x": dates,
                "y": pnl_values,
                "type": "scatter",
                "mode": "lines+markers",
                "name": "Net PnL"
            }
        ],
        "layout": {
            "title": "Net PnL Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "PnL ($)"}
        }
    }

    # 🧮 Get Alpaca PnL
    alpaca = get_alpaca_pnl()

    return render_template("dashboard.html", gpt_summary=gpt_summary, chart_data=json.dumps(chart_data), alpaca=alpaca)

if __name__ == "__main__":
    app.run(debug=True, port=7860)
