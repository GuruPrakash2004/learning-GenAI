import os
from dotenv import load_dotenv
from google import genai
from model import SupportResponse
import asyncio


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= api_key)


async def process_customer(c_name, message):
    chat = client.aio.chats.create(
       model="gemini-3-flash-preview",
        config={
            "system_instruction" : """
            You are a professional customer support assistant.
            Your responsibilities:
            - Be polite and professional.
            - Understand the customer's problem.
            - Do not invent information.
            - Do not claim that you performed an action
              unless the application actually performed it.
            - Keep the response in 10 to 15 words.
            """,
            # "response_mime_type": "application/json",
            # "response_schema": SupportResponse
        }
    )
    response = await chat.send_message(message)
    return c_name, response.text




# first chat gobal
chat = client.aio.chats.create(
    model="gemini-3-flash-preview",
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



async def main():

    customers = [
    ("Customer 1", "I was charged twice for my subscription"),
    ("Customer 2", "I forgot my password and cannot login"),
    ("Customer 3", "I cannot download my invoice")
    ]

    results = await asyncio.gather(
        *(process_customer(c_name,message)  for c_name, message in customers)
    )


    for c_name, message in results:
        print("-" * 60)
        print(f"{c_name} -> {message}")
       

    # while True:
    #     userInput = input("Customer:")
    #     if userInput.lower() == "exit":
    #         break
    #     response  = await chat.send_message(userInput)
    #     print(response.text)



if __name__ == "__main__":
    asyncio.run(main())

""" if response.text is None:
    print("No responce from API")
else:
    support_response = SupportResponse.model_validate_json(response.text)

    print( "Category",support_response.category)
    print( "Proirity",support_response.priority)
    print( "Message",support_response.message)

    if support_response.priority == "high":
        print("🚨 ACTION: Escalate this ticket to the support team.")

    elif support_response.priority == "medium":
        print("⚠️ ACTION: Add this ticket to the normal support queue.")

    else:
        print("✅ ACTION: No immediate escalation required.")

 """


# print(ressponce.text)

