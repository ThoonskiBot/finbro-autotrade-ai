import os
from datetime import datetime

required_files = [
    "tools/gpt_strategy_coach.py",
    "tools/gpt_weekly_reflector.py",
    "tools/strategy_alpha_recap.py",
    "tools/strategy_score_tracker.py",
    "tools/strategy_heatmap_generator.py",
    "tools/gpt_drift_summary.py",
    "tools/gpt_key_checker.py",
    "tools/send_full_weekly_report.py",
    "tools/send_gpt_coach_feedback.py",
    "tools/send_weekly_pdf_report.py",
    "tools/finbro_zip_backup.py",
    "tools/strategy_drift_preview.py"
]

status = []
base = "C:/FINBRO"

for file in required_files:
    full = os.path.join(base, file.replace("/", os.sep))
    exists = os.path.exists(full)
    status.append((file, "✅" if exists else "❌"))

print("=== FINBRO GO LIVE CHECK ===")
for file, flag in status:
    print(f"{flag} {file}")

print("\n📅 " + datetime.now().strftime("Last verified: %Y-%m-%d %H:%M:%S"))
