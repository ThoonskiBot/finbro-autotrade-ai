
from alpaca_trade_api.rest import REST
from core.config import APCA_API_KEY_ID as ALPACA_KEY, APCA_API_SECRET_KEY as ALPACA_SECRET, ALPACA_ENDPOINT

def get_live_positions():
    api = REST(ALPACA_KEY, ALPACA_SECRET, ALPACA_ENDPOINT)
    positions = api.list_positions()
    return {p.symbol: p.qty for p in positions}
