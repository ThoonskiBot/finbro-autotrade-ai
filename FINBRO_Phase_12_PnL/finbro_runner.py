from scripts.data_downloader_and_renamer import generate_signals
from executors.place_batch_orders_with_log import place_orders
from reports.pnl_summary import summarize_pnl
from core.config import LIVE_MODE

def run_finbro():
    print("🚀 FINBRO Trader with P&L Tracking")
    print(f"🔒 LIVE MODE: {'ENABLED' if LIVE_MODE else 'DISABLED'}\n")

    generate_signals()
    place_orders()
    summarize_pnl()

    print("\n✅ FINBRO Run Complete.")

if __name__ == "__main__":
    run_finbro()
