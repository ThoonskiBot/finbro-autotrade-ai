import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.data_downloader_and_renamer import generate_signals
from executors.place_batch_orders_with_log import place_orders
from reports.daily_trade_summary import generate_pdf_report
from core.config import LIVE_MODE

def run_finbro():
    print("🚀 FINBRO: Position + Live Price + PDF Report")
    print(f"🔒 LIVE MODE: {'ENABLED' if LIVE_MODE else 'DISABLED'}\n")

    generate_signals()
    place_orders()
    generate_pdf_report()

    print("\n✅ FINBRO Run Complete.")

if __name__ == "__main__":
    run_finbro()
