import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI")
)


models_to_test = [

    # Gemini 2.5
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",

    # Gemini 3
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash",

    # Preview
    "gemini-3.1-pro-preview",
    "gemini-3-flash-preview",
]


print("Testing available text models...\n")


for model_id in models_to_test:

    try:

        response = client.models.generate_content(
            model=model_id,
            contents="Say hello in one word",
        )

        text_output = response.text or ""

        if text_output:

            print(f"✅ WORKING: {model_id}")
            print(f"   Response: {text_output.strip()}\n")

        else:

            print(f"⚠️ RETURNED EMPTY: {model_id}\n")


    except Exception as e:

        print(f"❌ FAILED: {model_id}")
        print(f"   Error: {e}\n")