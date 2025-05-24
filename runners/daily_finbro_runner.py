
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess

print("🚀 Starting FINBRO Daily Runner...\n")

steps = [
    ("Placing batch bracket orders (with logging)", "executors/place_batch_orders_with_log.py"),
    ("Generating daily trade digest PDF", "reports/daily_trade_digest_generator.py"),
    ("Printing trade performance summary", "reports/trade_performance_summary.py")
]

for description, script in steps:
    print(f"➡️ {description}")
    try:
        subprocess.run(["python", script], check=True)
        print(f"✅ {script} completed successfully\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}\n")

print("🎯 FINBRO Daily Pipeline Complete!")
