import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key= api)

# Start a chat session
chat = client.chats.create(model="gemini-3.6-flash")

# Send message
response = chat.send_message("Hello, Gemini!")

print(response.text)