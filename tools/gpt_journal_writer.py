import os
from datetime import datetime
from dotenv import load_dotenv
import openai

load_dotenv(dotenv_path="C:/FINBRO/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

REPORTS_DIR = "C:/FINBRO/reports"
files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_risk_review_")], reverse=True)
if not files:
    print("❌ No risk review file found.")
    exit()

latest_file = files[0]
file_path = os.path.join(REPORTS_DIR, latest_file)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You're a trading assistant that journals market insights."},
        {"role": "user", "content": f"Based on this GPT risk review, write a daily market journal entry:

{content}"}
    ]
)

summary = response['choices'][0]['message']['content']
out_path = os.path.join(REPORTS_DIR, f"gpt_daily_journal_{datetime.now().strftime('%Y-%m-%d')}.txt")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(summary)

print(f"📝 GPT journal saved to: {out_path}")
