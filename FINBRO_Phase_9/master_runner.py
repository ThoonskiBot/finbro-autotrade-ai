import subprocess

print("🚀 Starting FINBRO Daily Runner...")

# Step 1: Generate fresh signals
print("\n➡️ Generating signals")
subprocess.run(["python", "scripts/data_downloader_and_renamer.py"], check=True)

# Step 2: Place orders using latest signals
print("\n➡️ Placing batch bracket orders (with logging)")
subprocess.run(["python", "executors/place_batch_orders_with_log.py"], check=True)

# Step 3: Generate daily digest
print("\n➡️ Generating daily trade digest PDF")
subprocess.run(["python", "reports/daily_trade_digest_generator.py"], check=True)

print("\n✅ FINBRO Daily Run Complete.")
