import requests
import time

price_cache = {}

def get_price(ticker):
    now = time.time()
    if ticker in price_cache:
        price, timestamp = price_cache[ticker]
        if now - timestamp < 30:
            return price

    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1m&range=1d"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        candles = data["chart"]["result"][0]["indicators"]["quote"][0]
        close_prices = candles["close"]
        if close_prices:
            latest = [c for c in close_prices if c is not None][-1]
            price_cache[ticker] = (latest, now)
            return float(latest)
    except Exception as e:
        print(f"❌ Failed to fetch Yahoo price for {ticker}: {e}")

    return 0.0
