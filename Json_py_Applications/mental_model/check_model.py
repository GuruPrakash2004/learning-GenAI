import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

models_to_test = [
    "gemini-2.5-flash",
    "models/gemini-2.5-flash",
    "gemini-2.5-pro",
    "models/gemini-2.5-pro",
    "gemini-3.6-flash",
    "models/gemini-3.6-flash",
    "gemini-3.5-flash",
    "models/gemini-3.5-flash",
]

print("Testing available text models...\n")

for model_id in models_to_test:
    try:
        response = client.models.generate_content(
            model=model_id,
            contents="Say hello in one word",
        )
        
        # Safe access to text with fallback if response.text is None
        text_output = response.text or ""
        
        if text_output:
            print(f"✅ WORKING: {model_id}")
            print(f"   Response: {text_output.strip()}\n")
            break
        else:
            print(f"⚠️ RETURNED EMPTY: {model_id}\n")
            
    except Exception as e:
        print(f"❌ FAILED: {model_id} -> {e}\n")