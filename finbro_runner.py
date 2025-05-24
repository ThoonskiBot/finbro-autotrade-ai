import json
import os

CONFIG_PATH = "config/strategy_config.json"

# Load strategy toggles
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
else:
    config = {"Momentum": True, "Reversal": True, "Neutral": True}

strategies = {
    "Momentum": lambda: print("Running Momentum Strategy"),
    "Reversal": lambda: print("Running Reversal Strategy"),
    "Neutral": lambda: print("Running Neutral Strategy")
}

print("🚀 FINBRO Execution Starting...")

for name, func in strategies.items():
    if config.get(name, False):
        print(f"✅ Executing {name}")
        func()
    else:
        print(f"⛔ Skipping {name} (Disabled)")

print("✅ FINBRO Strategy Execution Complete.")