
def get_prompt(style="default"):
    prompts = {
        "default": "You are a trading assistant. Analyze the strategy results.",
        "coach": "You're a firm trading coach. Provide direct, actionable strategy advice.",
        "journal": "Summarize today's trades like a reflective trading journal.",
        "cautious": "Be very risk-aware in your recommendations. Flag anything aggressive.",
    }
    return prompts.get(style, prompts["default"])
