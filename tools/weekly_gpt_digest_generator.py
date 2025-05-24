
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime, timedelta
from core.config import REPORTS_PATH

def generate_weekly_gpt_digest():
    print("📚 Generating Weekly GPT Summary Digest...")

    files = []
    today = datetime.now()
    cutoff_date = today - timedelta(days=7)

    # Gather last 7 days of GPT summaries
    for filename in sorted(os.listdir(REPORTS_PATH)):
        if filename.startswith("gpt_trade_summary_") and filename.endswith(".txt"):
            date_str = filename.replace("gpt_trade_summary_", "").replace(".txt", "")[:10]
            try:
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                if file_date >= cutoff_date:
                    files.append(os.path.join(REPORTS_PATH, filename))
            except:
                continue

    if not files:
        print("❌ No GPT summaries found in the last 7 days.")
        return

    digest_path = os.path.join(REPORTS_PATH, f"weekly_digest_{today.strftime('%Y-%m-%d')}.txt")
    with open(digest_path, "w", encoding="utf-8") as out_file:
        out_file.write("📆 WEEKLY GPT SUMMARY DIGEST\n\n")
        for file in files:
            out_file.write(f"--- {os.path.basename(file)} ---\n")
            with open(file, "r", encoding="utf-8") as f:
                out_file.write(f.read())
            out_file.write("\n\n")

    print(f"✅ Weekly GPT digest saved to: {digest_path}")

generate_weekly_gpt_digest()
