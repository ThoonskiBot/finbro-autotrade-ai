# Phase 121 – Strategy-to-Strategy Signal Translator
def translate_signal_format(signal, format_map):
    return {format_map.get(k, k): v for k, v in signal.items()}