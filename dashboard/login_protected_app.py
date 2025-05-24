from flask import Flask, render_template, request, redirect, url_for, session
import json
from pathlib import Path

app = Flask(__name__, static_folder="../reports", static_url_path="/static")
app.secret_key = "FINBRO_SECRET_KEY"

USERNAME = "admin"
PASSWORD = "finbro123"

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            return "<h3>Login failed. Try again.</h3>"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    gpt_file = Path("../reports/gpt_trade_summary_2025-05-21_1407.txt")
    gpt_summary = gpt_file.read_text() if gpt_file.exists() else "No GPT summary found."

    chart_data = {
        "data": [
            {
                "x": ["2025-05-19", "2025-05-20", "2025-05-21"],
                "y": [150, 170, 160],
                "type": "scatter",
                "mode": "lines+markers",
                "name": "PnL ($)"
            }
        ],
        "layout": {
            "title": "Net PnL Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "PnL"}
        }
    }

    return render_template("dashboard.html", gpt_summary=gpt_summary, chart_data=json.dumps(chart_data))

if __name__ == "__main__":
    app.run(debug=True, port=7860)
