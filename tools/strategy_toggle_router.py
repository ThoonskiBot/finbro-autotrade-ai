
import json
import os

def should_run(strategy_name):
    config_path = "C:/FINBRO/config/strategy_states.json"
    if not os.path.exists(config_path):
        return True
    with open(config_path, "r") as f:
        config = json.load(f)
    return config.get(strategy_name, True)
