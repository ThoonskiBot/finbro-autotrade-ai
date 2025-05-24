# Enhanced GPT Insight Logic
print('✅ GPT Insight Logic Running')
import os

log_path = 'logs/signal_log.csv'
if not os.path.exists(log_path):
    print("⚠️ No signal log found to summarize.")
else:
    print(f"📄 Summarizing signal log at: {log_path}")
    print("🧠 [GPT simulated] Top pattern: breakout after high momentum, fade after gap open.")