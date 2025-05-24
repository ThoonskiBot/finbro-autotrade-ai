
def handle_why_command(text, log_text, openai_api_key):
    import openai
    openai.api_key = openai_api_key

    question = "Why did we skip " + text.split("/why ")[-1].strip() + "?"
    messages = [
        {"role": "system", "content": "You are a trade analyst reviewing skipped trades."},
        {"role": "user", "content": question + "\n\n" + log_text}
    ]
    try:
        response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"GPT error: {e}"
