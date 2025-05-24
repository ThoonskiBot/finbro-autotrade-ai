import subprocess
from alerts.email_alert import send_trade_summary

print("🚀 Starting FINBRO Daily Runner...")

try:
    print("\n➡️ Generating signals")
    subprocess.run(["python", "scripts/data_downloader_and_renamer.py"], check=True)

    print("\n➡️ Placing batch bracket orders (with logging)")
    subprocess.run(["python", "executors/place_batch_orders_with_log.py"], check=True)

    print("\n➡️ Generating daily trade digest PDF")
    subprocess.run(["python", "reports/daily_trade_digest_generator.py"], check=True)

    print("\n📧 Sending trade summary email")
    send_trade_summary("logs")

    print("\n✅ FINBRO Daily Run Complete.")

except subprocess.CalledProcessError as e:
    print(f"❌ Error during execution: {e}")
