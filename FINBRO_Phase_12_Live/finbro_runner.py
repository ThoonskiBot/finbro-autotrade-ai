from scripts.data_downloader_and_renamer import generate_signals
from executors.place_batch_orders_with_log import place_orders
from reports.daily_trade_digest_generator import generate_digest
from alerts.email_alert import send_trade_summary
from core.config import LIVE_MODE

def run_finbro():
    print("🚀 Starting FINBRO Daily Runner...\n")
    print(f"🔒 LIVE MODE: {'ENABLED' if LIVE_MODE else 'DISABLED'}")

    print("\n➡️ Generating signals")
    generate_signals()

    print("\n➡️ Placing orders (LIVE = {})".format(LIVE_MODE))
    place_orders()

    print("\n➡️ Generating daily trade digest PDF")
    generate_digest()

    print("\n📧 Sending trade summary email")
    send_trade_summary("logs")

    print("\n✅ FINBRO Daily Run Complete.")

if __name__ == "__main__":
    run_finbro()
