import openai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

LOG_DIR = os.getenv("LOG_PATH", "C:/FINBRO/logs")

def promote_strategy(logs_folder=LOG_DIR):
    print(f"🔍 Scanning log folder: {logs_folder}")
    log_path = Path(logs_folder)
    log_files = sorted(log_path.glob("log_*.txt"))

    if not log_files:
        print("⚠️ No log_*.txt files found. Checking for any *.txt logs instead...")
        log_files = sorted(log_path.glob("*.txt"))

    if not log_files:
        print("❌ Still no logs found.")
        return "⚠️ No logs found."

    full_text = ""
    for f in log_files:
        try:
            text = f.read_text(encoding="utf-8").strip()
            print(f"📄 Reading {f.name}: {len(text)} chars")
            if text:
                full_text += f"--- {f.name} ---\n{text}\n"
        except Exception as e:
            print(f"❌ Failed to read {f.name}: {e}")

    if not full_text:
        print("❌ All logs are empty.")
        return "⚠️ All logs are empty."

    prompt = (
        "Based on the last few days of stock trading logs, which strategy performed best? "
        "Recommend one to promote for tomorrow with a short reason.\n\n"
        f"{full_text}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
        )
        print("✅ GPT strategy selection completed.")
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ GPT Error: {e}")
        return f"❌ GPT Error: {e}"