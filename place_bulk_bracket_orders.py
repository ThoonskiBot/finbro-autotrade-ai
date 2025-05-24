
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_ENDPOINT")

# Connect to Alpaca
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Load latest signal file from signals/ folder
def get_latest_signal_file():
    import glob
    files = glob.glob("signals/signals_*.csv")
    if not files:
        print("❌ No signal files found.")
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

# Place bracket orders from signals
def place_bracket_orders(signal_file, qty=10, tp_pct=3.0, sl_pct=2.0):
    df = pd.read_csv(signal_file)
    tickers = df['Ticker'].dropna().unique()

    for symbol in tickers:
        try:
            last_quote = api.get_latest_quote(symbol)
            ask_price = float(last_quote.ask_price)
            if ask_price == 0.0:
                print(f"⚠️ Skipping {symbol}: No valid ask price")
                continue

            # Calculate bracket levels
            tp = round(ask_price * (1 + tp_pct / 100), 2)
            sl = round(ask_price * (1 - sl_pct / 100), 2)

            order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side='buy',
                type='limit',
                time_in_force='gtc',
                limit_price=ask_price,
                order_class='bracket',
                take_profit={'limit_price': tp},
                stop_loss={'stop_price': sl}
            )

            print(f"✅ {symbol} | Entry: ${ask_price} | TP: ${tp} | SL: ${sl} | Order ID: {order.id}")

        except Exception as e:
            print(f"❌ Error placing order for {symbol}: {e}")

# Execute
signal_file = get_latest_signal_file()
if signal_file:
    print(f"📊 Using signal file: {signal_file}")
    place_bracket_orders(signal_file)
