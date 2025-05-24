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
    print(f"🔍 Checking log dir: {LOG_DIR}")
    logs = sorted(Path(LOG_DIR).glob("log_*.txt"))
    if not logs:
        all_logs = sorted(Path(LOG_DIR).glob("*.txt"))
        print(f"Fallback logs found: {[f.name for f in all_logs]}")
        return all_logs[-1] if all_logs else None
    print(f"Latest log file: {logs[-1].name}")
    return logs[-1]

def reflect_on_day():
    log_file = get_latest_log_file()
    if not log_file or not log_file.exists():
        print("❌ No log file found.")
        return "⚠️ No log found."

    text = log_file.read_text(encoding="utf-8").strip()
    print(f"📄 Log Content ({log_file.name}):\n{text}")

    if not text:
        print("❌ Log file is empty.")
        return "⚠️ Log file is empty."

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
        print(f"✅ Reflection written to {outfile}")
        return str(outfile)
    except Exception as e:
        print(f"❌ GPT error: {e}")
        return f"❌ GPT Error: {e}"