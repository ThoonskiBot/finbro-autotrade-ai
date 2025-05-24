# Phase 116 – Strategy Memory Bank

def store_strategy_memory(memory, session_data):
    memory.append(session_data)
    return memory[-5:]  # keep last 5 sessions