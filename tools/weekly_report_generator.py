
import os
from datetime import datetime
from core.config import LOG_PATH, REPORTS_PATH

def generate_weekly_report():
    files = sorted([f for f in os.listdir(LOG_PATH) if f.startswith("order_log_")], reverse=True)[:5]
    report_lines = []

    for file in files:
        report_lines.append(f"📅 {file}")
        with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
            report_lines.extend(f.readlines())
        report_lines.append("\n")

    path = os.path.join(REPORTS_PATH, f"weekly_trade_digest_{datetime.now().strftime('%Y-%m-%d')}.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.writelines(report_lines)

    print(f"✅ Weekly report saved to: {path}")

if __name__ == "__main__":
    generate_weekly_report()
