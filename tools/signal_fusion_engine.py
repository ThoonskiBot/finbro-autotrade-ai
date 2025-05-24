"""
FINBRO Signal Fusion Engine (Patched)

This module combines multiple signal sources into a final unified decision.
Safely skips malformed signals.
"""

def fuse_signals(signal_list):
    """
    Simple fusion logic: majority vote or average confidence
    :param signal_list: list of signal dicts, each with 'ticker', 'action', 'confidence'
    :return: fused signal list
    """
    from collections import defaultdict, Counter

    fused = defaultdict(lambda: {"buy": 0, "sell": 0, "hold": 0, "conf": []})
    skipped = 0

    for signal in signal_list:
        try:
            t = signal["ticker"]
            a = signal["action"]
            c = signal.get("confidence", 1.0)
            fused[t][a] += 1
            fused[t]["conf"].append(c)
        except KeyError:
            skipped += 1
            continue

    result = []
    for ticker, votes in fused.items():
        action = max(["buy", "sell", "hold"], key=lambda x: votes[x])
        avg_conf = round(sum(votes["conf"]) / len(votes["conf"]), 3)
        result.append({"ticker": ticker, "action": action, "confidence": avg_conf})

    print(f"✅ Signal fusion complete. Skipped {skipped} malformed signals.")
    return result
