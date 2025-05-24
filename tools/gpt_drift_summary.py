import os
from datetime import datetime
from dotenv import load_dotenv
import openai

load_dotenv("C:/FINBRO/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

REPORT_DIR = "C:/FINBRO/reports"
delta_file = sorted([f for f in os.listdir(REPORT_DIR) if f.startswith("log_diff_")], reverse=True)
tracker_file = sorted([f for f in os.listdir(REPORT_DIR) if f.startswith("strategy_score_tracker_")], reverse=True)

if not delta_file or not tracker_file:
    print("❌ Missing delta or tracker data.")
    exit()

with open(os.path.join(REPORT_DIR, delta_file[0]), "r", encoding="utf-8") as f:
    delta_content = f.read()
with open(os.path.join(REPORT_DIR, tracker_file[0]), "r", encoding="utf-8") as f:
    tracker_content = f.read()

prompt = f"""You're an elite trading strategy analyst. Based on the strategy tracker and trade log differences:

=== STRATEGY SCORE TRACKER ===
{tracker_content}

=== LOG DELTA ===
{delta_content}

Write a 3-part analysis:
1. Summary of change in trade behavior
2. Risk or drift detected
3. 2 action steps for next week"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a professional trading strategy auditor."},
        {"role": "user", "content": prompt}
    ]
)

summary = response['choices'][0]['message']['content']
filename = f"gpt_trade_drift_summary_{datetime.now().strftime('%Y-%m-%d')}.txt"
with open(os.path.join(REPORT_DIR, filename), "w", encoding="utf-8") as f:
    f.write(summary)

print(f"✅ GPT Drift Summary saved to: C:/FINBRO/reports/{filename}")
