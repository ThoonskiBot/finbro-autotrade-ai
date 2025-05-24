
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_ENDPOINT")

# Alpaca API setup
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# === CONFIG ===
# Map your file to a known ticker (recommended you follow this naming pattern)
TICKER = "SPY"
SIGNAL_FILE = "signals/signals_20250520_114232.csv"
QTY = 10
TP_PCT = 3.0  # 3% take profit
SL_PCT = 2.0  # 2% stop loss

# Load the signal data
df = pd.read_csv(SIGNAL_FILE)

# Get the latest price from the CSV
if df.empty:
    print(f"❌ Signal file is empty: {SIGNAL_FILE}")
else:
    latest_close = df['Close'].iloc[-1]
    entry_price = round(latest_close, 2)
    take_profit = round(entry_price * (1 + TP_PCT / 100), 2)
    stop_loss = round(entry_price * (1 - SL_PCT / 100), 2)

    try:
        order = api.submit_order(
            symbol=TICKER,
            qty=QTY,
            side='buy',
            type='limit',
            time_in_force='gtc',
            limit_price=entry_price,
            order_class='bracket',
            take_profit={'limit_price': take_profit},
            stop_loss={'stop_price': stop_loss}
        )
        print(f"✅ Bracket order placed for {TICKER} | Entry: ${entry_price} | TP: ${take_profit} | SL: ${stop_loss}")
        print(f"🆔 Order ID: {order.id}")

    except Exception as e:
        print(f"❌ Failed to place bracket order: {e}")
