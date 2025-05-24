import os
import openai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

LOG_DIR = os.getenv("LOG_PATH", "logs")

def get_last_n_logs(n=7):
    log_files = sorted(Path(LOG_DIR).glob("log_*.txt"))[-n:]
    return log_files

def summarize_drift():
    log_files = get_last_n_logs()
    if not log_files:
        return "⚠️ No logs found for drift detection."

    all_logs = ""
    for file in log_files:
        all_logs += f"--- {file.name} ---\n"
        all_logs += file.read_text(encoding="utf-8") + "\n"

    prompt = (
        "You're FINBRO's strategy analyst. Review the following logs from the last 7 days "
        "and summarize any strategic drift, changes in trade behavior, and performance trends:\n\n"
        f"{all_logs}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {str(e)}"