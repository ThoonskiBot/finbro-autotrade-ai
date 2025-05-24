
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template_string, request, Response
from core.config import REPORTS_PATH, DASHBOARD_USER, DASHBOARD_PASS
from datetime import datetime
import base64
from io import BytesIO

app = Flask(__name__)

def check_auth(username, password):
    return username == DASHBOARD_USER and password == DASHBOARD_PASS

def authenticate():
    return Response(
        'Authentication required.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def get_gpt_summary():
    today_str = datetime.now().strftime("%Y-%m-%d")
    for file in os.listdir(REPORTS_PATH):
        if today_str in file and "gpt_trade_summary" in file:
            with open(os.path.join(REPORTS_PATH, file), "r", encoding="utf-8") as f:
                return f.read()
    return "No GPT summary found for today."

def get_sample_chart():
    try:
        from tools.performance_plotter import generate_pnl_chart
        chart = generate_pnl_chart()
        if chart:
            return chart
        else:
            return "data:image/png;base64,"  # blank chart fallback
    except Exception as e:
        print("⚠️ Failed to generate PnL chart:", e)
        return "data:image/png;base64,"

@app.route("/")
@requires_auth
def dashboard():
    summary = get_gpt_summary()
    chart = get_sample_chart()
    return render_template_string("""
    <html>
    <head><title>FINBRO Dashboard</title></head>
    <body style='font-family:Arial;padding:20px;'>
        <h2>📊 FINBRO Secure Dashboard</h2>
        <h3>🧠 GPT Summary</h3>
        <pre style='background:#f4f4f4;padding:10px;'>{{ summary }}</pre>
        <h3>💹 Performance Chart</h3>
        <img src="{{ chart }}" alt="Chart">
    </body>
    </html>
    """, summary=summary, chart=chart)

if __name__ == "__main__":
    app.run(debug=True)
