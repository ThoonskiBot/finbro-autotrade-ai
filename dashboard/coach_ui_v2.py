
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, render_template_string
from tools.trade_llm_coach import ask_trade_question
from core.config import LOG_PATH

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def ask():
    response = ""
    preset = request.args.get("preset", "")
    if request.method == "POST":
        question = request.form.get("question", "")
        latest_log = sorted([f for f in os.listdir(LOG_PATH) if f.startswith("order_log_")], reverse=True)[0]
        with open(os.path.join(LOG_PATH, latest_log), "r", encoding="utf-8") as f:
            log_text = f.read()
        response = ask_trade_question(question, log_text)
    return render_template_string("""
        <form method="POST">
            <h2>🧠 FINBRO Coach GPT 2.0</h2>
            <input name="question" value="{{preset}}" style="width:80%%" placeholder="Ask your question...">
            <button type="submit">Ask</button>
        </form>
        <pre>{{response}}</pre>
        <hr>
        <a href="/?preset=What strategy performed best?">📈 What strategy performed best?</a><br>
        <a href="/?preset=Why did we skip TSLA today?">🤔 Why did we skip TSLA today?</a><br>
        <a href="/?preset=Should I scale down Reversal?">📉 Should I scale down Reversal?</a>
    """, preset=preset, response=response)

if __name__ == "__main__":
    app.run(port=5051, debug=True)
