
import requests

def get_price(ticker):
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}")
        data = r.json()["quoteResponse"]["result"][0]
        price = data["regularMarketPrice"]
        change = data["regularMarketChangePercent"]
        return f"📈 {ticker.upper()} = ${price:.2f} ({change:+.2f}%)"
    except Exception as e:
        return f"❌ Could not fetch {ticker}: {e}"
