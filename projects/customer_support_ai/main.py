import os
from dotenv import load_dotenv
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

userInput = input("Customer:")

ressponce = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=userInput
)

print(ressponce.text)

