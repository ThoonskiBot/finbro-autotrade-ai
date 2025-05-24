
# tools/gpt_trade_coach.py

import os
import openai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
LOG_DIR = os.getenv("LOG_PATH", "logs")

def get_latest_log_file():
    log_files = sorted(Path(LOG_DIR).glob("log_*.txt"))
    return log_files[-1] if log_files else None

def coach_trades():
    log_path = get_latest_log_file()
    if not log_path:
        return "⚠️ No trade logs found for coaching."

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.read()[-3000:]

    prompt = (
        "You're a seasoned trading coach. A user asked for professional feedback on this trade log.

"
        "Please highlight common mistakes, good trades, and strategic improvements:

"
        f"{lines}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {str(e)}"
