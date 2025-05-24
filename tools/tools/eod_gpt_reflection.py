# tools/eod_gpt_reflection.py

import os
import openai
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
LOG_DIR = os.getenv("LOG_PATH", "logs")
REFLECTION_DIR = os.getenv("REFLECTION_PATH", "reports")

def get_latest_log_file():
    logs = sorted(Path(LOG_DIR).glob("log_*.txt"))
    return logs[-1] if logs else None

def reflect_on_day():
    log_file = get_latest_log_file()
    if not log_file:
        return "⚠️ No log found."
    text = log_file.read_text()
    prompt = f"Summarize today’s stock trading log and reflect on what went well, what didn't, and what to improve.\n\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
        reflection = response.choices[0].message.content.strip()
        outfile = Path(REFLECTION_DIR) / f"eod_reflection_{datetime.now().strftime('%Y-%m-%d')}.txt"
        outfile.parent.mkdir(parents=True, exist_ok=True)
        outfile.write_text(reflection)
        return str(outfile)
    except Exception as e:
        return f"❌ GPT Error: {e}"