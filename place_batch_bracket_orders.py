
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import glob

# Load environment variables
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_ENDPOINT")

# Alpaca API setup
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# === CONFIG ===
SIGNALS_DIR = "signals/"
QTY = 10
TP_PCT = 3.0  # 3% take profit
SL_PCT = 2.0  # 2% stop loss

def infer_ticker_from_filename(filename):
    basename = os.path.basename(filename)
    parts = basename.replace(".csv", "").split("_")
    for part in parts:
        if part.isalpha() and len(part) <= 5:  # crude ticker check
            return part.upper()
    return None

def process_signal_file(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty or 'Close' not in df.columns:
            print(f"⚠️ Skipping {file_path} (empty or invalid format)")
            return

        latest_close = df['Close'].iloc[-1]
        entry_price = round(latest_close, 2)
        take_profit = round(entry_price * (1 + TP_PCT / 100), 2)
        stop_loss = round(entry_price * (1 - SL_PCT / 100), 2)
        ticker = infer_ticker_from_filename(file_path)

        if not ticker:
            print(f"❌ Could not infer ticker from filename: {file_path}")
            return

        order = api.submit_order(
            symbol=ticker,
            qty=QTY,
            side='buy',
            type='limit',
            time_in_force='gtc',
            limit_price=entry_price,
            order_class='bracket',
            take_profit={'limit_price': take_profit},
            stop_loss={'stop_price': stop_loss}
        )

        print(f"✅ {ticker} | Entry: ${entry_price} | TP: ${take_profit} | SL: ${stop_loss} | Order ID: {order.id}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

# Main execution loop
signal_files = glob.glob(os.path.join(SIGNALS_DIR, "*.csv"))
if not signal_files:
    print("❌ No signal files found in the 'signals/' directory.")
else:
    print(f"📂 Found {len(signal_files)} signal file(s). Processing...")
    for file_path in signal_files:
        process_signal_file(file_path)
