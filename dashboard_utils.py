
import json
from pathlib import Path

CONFIG_PATH = Path("C:/FINBRO/strategy_config.json")

def get_active_strategies():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return [k for k, v in json.load(f).items() if v]
    return ["momentum", "reversal", "neutral"]

def get_pnl():
    return {'date': '2025-05-23', 'pnl': 1325.40}
