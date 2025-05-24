# Summarizes weekly GPT trade summaries into one strategic digest
import os
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_weekly_gpt_digest(src_folder="reports", output="reports/gpt_weekly_digest.txt"):
    today = datetime.now().date()
    filenames = []

    for i in range(5):
        day = today - timedelta(days=i)
        for file in Path(src_folder).glob(f"gpt_trade_summary_{day}_*.txt"):
            filenames.append(file)

    if not filenames:
        print("❌ No GPT summary files found for the past 5 days.")
        return

    content = ""
    for file in sorted(filenames):
        content += f"--- {file.name} ---\n"
        content += file.read_text() + "\n\n"

    prompt = f"You're an AI trading strategist. Summarize and optimize this 5-day strategy:\n\n{content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600
        )
        summary = response.choices[0].message["content"]
        Path(output).write_text(summary)
        print(f"✅ Weekly GPT digest saved to: {output}")
    except Exception as e:
        print(f"❌ Failed to generate digest: {e}")

if __name__ == "__main__":
    generate_weekly_gpt_digest()
