
# Store different GPT prompt options here
def get_prompt(style="default"):
    prompts = {
        "default": "You are a trading assistant. Analyze the strategy results.",
        "coach": "You're a firm trading coach. Provide direct, actionable strategy advice.",
        "journal": "Summarize the trading activity like a journal entry.",
    }
    return prompts.get(style, prompts["default"])
