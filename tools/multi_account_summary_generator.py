# Phase 128 – Multi-Account Summary Generator

def summarize_accounts(accounts):
    summary = {}
    for acc, stats in accounts.items():
        summary[acc] = {
            "pnl": round(stats["pnl"], 2),
            "trades": stats["trades"],
            "win_rate": round(stats["wins"] / stats["trades"], 2) if stats["trades"] else 0
        }
    return summary