
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables from .env file
load_dotenv()

# Load API credentials
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_ENDPOINT")

# Connect to Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Try fetching account info
try:
    account = api.get_account()
    print(f"✅ Connected to Alpaca! Account ID: {account.id} | Status: {account.status} | Equity: ${account.equity}")
except Exception as e:
    print(f"❌ Failed to connect to Alpaca: {e}")
