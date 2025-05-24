import os
from dotenv import load_dotenv
from datetime import datetime
import openai

load_dotenv("C:/FINBRO/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"

# Collect last 10 trade logs
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith("order_log")], reverse=True)[:10]
log_summary = ""
for fname in files:
    log_summary += f"--- {fname} ---\\n"
    with open(os.path.join(LOG_DIR, fname), "r", encoding="utf-8") as f:
        log_summary += f.read() + "\\n"

if not log_summary.strip():
    print("❌ No log data to review.")
    exit()

prompt = (
    "You are a strategy coach. Analyze these trading logs for edge, confidence shifts, drift, or risk issues:\\n"
    + log_summary +
    "\\n\\nProvide a 1-paragraph summary and 3 actionable coaching points."
)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a highly experienced trading strategist and performance coach."},
        {"role": "user", "content": prompt}
    ]
)

feedback = response['choices'][0]['message']['content']
filename = f"gpt_coach_feedback_{datetime.now().strftime('%Y-%m-%d')}.txt"
with open(os.path.join(REPORT_DIR, filename), "w", encoding="utf-8") as f:
    f.write(feedback)

print(f"✅ GPT Strategy Coach feedback saved to: C:/FINBRO/reports/{filename}")
