import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get the API key explicitly from .env
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client directly with key
client = genai.Client(api_key=api_key)

# Use gemini-3.6-flash
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hello, Gemini!",
)

print(response.text)