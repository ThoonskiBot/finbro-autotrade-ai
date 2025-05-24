import os
from dotenv import load_dotenv
import openai

load_dotenv("C:/FINBRO/.env")
key = os.getenv("OPENAI_API_KEY")

if not key:
    print("❌ OPENAI_API_KEY not found in .env")
    exit()

try:
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a diagnostic assistant."},
            {"role": "user", "content": "Return 'API key is working properly' if this request succeeds."}
        ]
    )
    print("✅", response["choices"][0]["message"]["content"])
except Exception as e:
    print(f"❌ GPT API check failed: {e}")
