import os
import sys
from pathlib import Path

# Make sure tools are importable
sys.path.append(os.path.abspath("."))

from tools.signal_scorer import score_signal
from tools.cloud_backup import backup_logs_to_local_cloud
from tools.eod_gpt_reflection import reflect_on_day
from tools.strategy_promoter import promote_strategy

print("\n🚀 FINBRO Phase 77–80 Test Launcher")

# Phase 77: GPT Signal Scoring
print("\n🧠 Phase 77: Scoring signal 'AAPL' with sample context...")
context = "Signal triggered by RSI < 30 and SPY trend confirmation."
score = score_signal("AAPL", context)
print(f"Score: {score}")

# Phase 78: Cloud Backup
print("\n☁️ Phase 78: Backing up trade logs...")
backup_path = backup_logs_to_local_cloud()
print(f"Logs backed up to: {backup_path}")

# Phase 79: End-of-Day Reflection
print("\n📘 Phase 79: Generating GPT reflection on today’s log...")
reflection_result = reflect_on_day()
print(f"Reflection saved to: {reflection_result}")

# Phase 80: Strategy Promotion
print("\n📈 Phase 80: Promoting best strategy from logs...")
strategy = promote_strategy()
print(f"Promotion Result: {strategy}")

print("\n✅ All Phase 77–80 functions tested.")