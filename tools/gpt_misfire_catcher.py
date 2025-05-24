# Phase 117 – GPT Misfire Catcher

def detect_gpt_misfire(signal, outcome):
    return signal.get("confidence", 1) > 0.75 and outcome == "loss"