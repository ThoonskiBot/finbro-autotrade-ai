
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load .env variables
load_dotenv()

# API Credentials
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_ENDPOINT")

# Connect to Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# === CONFIGURE YOUR TRADE ===
symbol = "SPY"  # Ticker to trade
qty = 10        # Number of shares
entry_price = 500.00  # Entry limit price
take_profit = 515.00  # Take profit limit price
stop_loss = 490.00    # Stop loss stop price

# Submit the bracket order
try:
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        time_in_force='gtc',
        limit_price=entry_price,
        order_class='bracket',
        take_profit={'limit_price': take_profit},
        stop_loss={'stop_price': stop_loss}
    )
    print(f"✅ Bracket order placed for {symbol} at ${entry_price} | TP: ${take_profit}, SL: ${stop_loss}")
    print(f"🆔 Order ID: {order.id}")
except Exception as e:
    print(f"❌ Failed to place bracket order: {e}")
