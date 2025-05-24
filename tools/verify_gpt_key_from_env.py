import os
from dotenv import load_dotenv
import openai

load_dotenv("C:/FINBRO/.env")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key or api_key.strip() == "":
    print("❌ OPENAI_API_KEY is missing or blank in your .env")
    exit()

try:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a diagnostic assistant."},
            {"role": "user", "content": "Reply exactly: ✅ API key is working properly"}
        ]
    )
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"❌ GPT API failed: {e}")
