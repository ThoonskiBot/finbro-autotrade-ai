import os
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"
files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".txt")], reverse=True)[:7]

summary_input = ""
for fname in files:
    with open(os.path.join(LOG_DIR, fname), "r", encoding="utf-8") as f:
        summary_input += f"\n--- {fname} ---\n" + f.read()

if not summary_input.strip():
    print("❌ No log content found.")
    exit()

prompt = f"Summarize the performance, trends, and issues from this week's trade logs:\n{summary_input}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a quantitative trading coach."},
        {"role": "user", "content": prompt}
    ]
)

weekly_summary = response['choices'][0]['message']['content']
out_path = os.path.join(REPORT_DIR, f"gpt_weekly_reflection_{datetime.now().strftime('%Y-%m-%d')}.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(weekly_summary)

print(f"✅ Weekly GPT reflection saved to: {out_path}")
