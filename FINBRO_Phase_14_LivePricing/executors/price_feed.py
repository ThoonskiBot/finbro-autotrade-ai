import requests
import core.config as cfg

def get_price(ticker):
    url = f"{cfg.ALPACA_BASE_URL}/v2/stocks/{ticker}/quotes/latest"
    headers = {
        "APCA-API-KEY-ID": cfg.ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": cfg.ALPACA_SECRET_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data["askprice"])
    except Exception as e:
        print(f"❌ Failed to fetch price for {ticker}: {e}")
        return None
