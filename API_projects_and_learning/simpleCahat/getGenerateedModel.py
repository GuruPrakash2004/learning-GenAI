from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI")
)

print("Available models:\n")

for model in client.models.list():

    if model.supported_actions and "generateContent" in model.supported_actions:
        print(model.name)