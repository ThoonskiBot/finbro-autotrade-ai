# tools/strategy_promoter.py

import openai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def promote_strategy(logs_folder="logs"):
    log_files = sorted(Path(logs_folder).glob("log_*.txt"))[-5:]
    if not log_files:
        return "⚠️ No logs found."

    full_text = ""
    for f in log_files:
        full_text += f"--- {f.name} ---\n" + f.read_text() + "\n"

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
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {e}"