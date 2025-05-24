
import os
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from core.config import *

load_dotenv()

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_ENDPOINT, api_version='v2')

def place_bracket_order(symbol, price):
    tp = round(price * (1 + TP_PERCENT / 100), 2)
    sl = round(price * (1 - SL_PERCENT / 100), 2)
    order = api.submit_order(
        symbol=symbol,
        qty=DEFAULT_QTY,
        side='buy',
        type='limit',
        time_in_force='gtc',
        limit_price=price,
        order_class='bracket',
        take_profit={'limit_price': tp},
        stop_loss={'stop_price': sl}
    )
    return order

def main():
    signal_files = [f for f in os.listdir(SIGNALS_DIR) if f.endswith('.csv')]
    if not signal_files:
        print("❌ No signal files found.")
        return

    for file in signal_files:
        df = pd.read_csv(os.path.join(SIGNALS_DIR, file))
        if 'Close' not in df.columns:
            print(f"⚠️ Skipping {file} - no 'Close' column")
            continue

        last_close = df['Close'].iloc[-1]
        ticker = os.path.basename(file).split('_')[0].upper()
        order = place_bracket_order(ticker, last_close)
        print(f"✅ Order placed for {ticker} at ${last_close:.2f} | TP: ${order.take_profit['limit_price']} | SL: ${order.stop_loss['stop_price']}")

if __name__ == "__main__":
    main()
