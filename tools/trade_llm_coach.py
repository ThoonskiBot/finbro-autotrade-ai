
# GPT trade coach module — placeholder for question answering from logs
def ask_trade_question(question, log_text):
    import openai
    from core.config import OPENAI_API_KEY
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a FINBRO trade log coach. Answer with insights from the logs."},
            {"role": "user", "content": question + "\n\n" + log_text}
        ]
    )
    return response['choices'][0]['message']['content']
