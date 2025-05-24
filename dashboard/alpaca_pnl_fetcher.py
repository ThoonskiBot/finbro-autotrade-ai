# Fetches current Alpaca account PnL using your .env keys
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_alpaca_pnl():
    key_id = os.getenv("APCA_API_KEY_ID")
    secret = os.getenv("APCA_API_SECRET_KEY")
    endpoint = os.getenv("ALPACA_ENDPOINT", "https://paper-api.alpaca.markets")

    headers = {
        "APCA-API-KEY-ID": key_id,
        "APCA-API-SECRET-KEY": secret
    }

    try:
        res = requests.get(f"{endpoint}/v2/account", headers=headers)
        data = res.json()

        equity = float(data["equity"])
        last_equity = float(data["last_equity"])
        change = equity - last_equity

        return {
            "equity": round(equity, 2),
            "last_equity": round(last_equity, 2),
            "change": round(change, 2)
        }
    except Exception as e:
        return {"error": str(e)}
