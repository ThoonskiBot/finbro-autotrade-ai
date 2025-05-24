# Phase 115 – Trade Retry Manager (AI-guided placeholder logic)

def retry_trade(trade, reason):
    if "timeout" in reason.lower():
        trade['retry'] = True
        trade['adjustment'] = "delay 2s"
    elif "slippage" in reason.lower():
        trade['retry'] = True
        trade['adjustment'] = "reduce size by 10%"
    else:
        trade['retry'] = False
    return trade