import os
import sys
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from core.config import *

def generate_trade_orders():
    signal_dir = os.path.join(os.getcwd(), 'signals')
    latest_file = sorted([f for f in os.listdir(signal_dir) if f.endswith('.csv')])[-1]
    signal_path = os.path.join(signal_dir, latest_file)

    df = pd.read_csv(signal_path)
    print(f"📊 Loaded signals from: {latest_file}")

    orders = []

    for _, row in df.iterrows():
        side = row['Signal'].upper()
        if side not in ['BUY', 'SELL']:
            continue

        order = {
            "symbol": row['Ticker'],
            "qty": 50,
            "side": side.lower(),
            "type": "market",
            "time_in_force": "gtc"
        }
        orders.append(order)

    return orders
