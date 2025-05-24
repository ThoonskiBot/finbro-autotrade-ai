
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import openai
from datetime import datetime
from core.config import OPENAI_API_KEY, LOG_PATH, REPORTS_PATH

def generate_reflection():
    logs = sorted([f for f in os.listdir(LOG_PATH) if f.startswith("order_log_")], reverse=True)
    if not logs:
        return

    with open(os.path.join(LOG_PATH, logs[0]), "r", encoding="utf-8") as f:
        log_text = f.read()

    openai.api_key = OPENAI_API_KEY
    messages = [
        {"role": "system", "content": "Summarize today's trading activity like a reflective trading journal."},
        {"role": "user", "content": log_text}
    ]

    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    summary = response['choices'][0]['message']['content']

    path = os.path.join(REPORTS_PATH, f"gpt_reflection_{datetime.now().strftime('%Y-%m-%d')}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"✅ Reflection saved to: {path}")

if __name__ == "__main__":
    generate_reflection()
