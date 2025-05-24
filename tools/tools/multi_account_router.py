# Phase 91 – Multi-Account Strategy Router
def route_trade_by_account(signal, accounts):
    strategy = signal.get('strategy')
    return accounts.get(strategy, 'default')