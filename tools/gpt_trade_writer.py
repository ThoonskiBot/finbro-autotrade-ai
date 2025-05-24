
def write_trade_comment(signal, openai_api_key):
    import openai
    openai.api_key = openai_api_key
    prompt = f"Write a 1-sentence journal comment for this trade: {signal}"
    messages = [
        {"role": "system", "content": "You are a trader writing trade journal notes."},
        {"role": "user", "content": prompt}
    ]
    try:
        response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error writing GPT comment: {e}"
