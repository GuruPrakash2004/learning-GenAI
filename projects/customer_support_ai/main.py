import os
from dotenv import load_dotenv
from google import genai
from model import SupportResponse
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key= api_key)





userInput = input("Customer:")

ressponce = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=userInput,
    config={
        "system_instruction" : """
        You are a professional customer support assistant.

        Your responsibilities:
        - Be polite and professional.
        - Understand the customer's problem.
        - Give a helpful response.
        - Do not invent information.
        - Do not claim that you performed an action unless
            the application actually performed that action.
        - Do not claim to process refunds, contact teams,
            check accounts, or modify customer data.
        - Keep the response in 20 to 30 words.
        """,
        "response_mime_type": "application/json",
        "response_schema": SupportResponse

    }
)
if ressponce.text is None:
    print("No responce from API")
else:
    support_response = SupportResponse.model_validate_json(ressponce.text)

    print( "Category",support_response.category)
    print( "Proirity",support_response.priority)
    print( "Message",support_response.message)

    if support_response.priority == "high":
        print("🚨 ACTION: Escalate this ticket to the support team.")

    elif support_response.priority == "medium":
        print("⚠️ ACTION: Add this ticket to the normal support queue.")

    else:
        print("✅ ACTION: No immediate escalation required.")




# print(ressponce.text)

