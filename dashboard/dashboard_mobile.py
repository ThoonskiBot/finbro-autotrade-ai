
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template_string
from core.config import REPORTS_PATH
from dashboard.dashboard_saf_block import get_saf_dashboard_html
from dashboard.alpha_summary_block import get_alpha_summary_html
from dashboard.pnl_chart_block import get_latest_pnl_chart

app = Flask(__name__, static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static')))

def get_latest_summary():
    try:
        files = sorted([f for f in os.listdir(REPORTS_PATH) if f.startswith("gpt_trade_summary")], reverse=True)
        if not files:
            return "No summary available."
        path = os.path.join(REPORTS_PATH, files[0])
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Error loading summary."

@app.route("/")
def dashboard():
    summary = get_latest_summary()
    saf_html = get_saf_dashboard_html()
    alpha_html = get_alpha_summary_html()
    pnl_chart = get_latest_pnl_chart()

    return render_template_string("""
    <html>
    <head>
        <title>FINBRO Mobile Dashboard</title>
        <meta http-equiv="refresh" content="30">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #111;
                color: #eee;
                padding: 20px;
            }
            h2, h3 {
                color: #00ff99;
            }
            pre {
                background-color: #222;
                padding: 10px;
                border-radius: 5px;
            }
            img {
                border: 1px solid #444;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h2>📲 FINBRO Mobile Dashboard</h2>
        <h3>🧠 GPT Summary</h3>
        <pre>{{ summary }}</pre>

        {{ saf_html | safe }}
        {{ alpha_html | safe }}
        {{ pnl_chart | safe }}
    </body>
    </html>
    """, summary=summary, saf_html=saf_html, alpha_html=alpha_html, pnl_chart=pnl_chart)

if __name__ == "__main__":
    app.run(debug=True)
