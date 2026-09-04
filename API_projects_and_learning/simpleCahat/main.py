from dotenv import load_dotenv
import os 
from google import genai
from pydantic import BaseModel
from typing import Literal
from generateText import chatResponceHandeler


load_dotenv()
# get the key from env
api_key = os.getenv("GEMINI_API_KEY")
# create the client 
client = genai.Client(api_key=api_key);
# create chat for state maintain

class ResponceModel(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    priority: Literal["low","medium","high"]
    message: str


chat = client.chats.create(
    model="gemini-3.6-flash",
    config = {
    "system_instruction": """
    You are a professional softwate support assistant.
    
    Your responsibilities:
    - Answer customers politely and empathetically
    - Understand their grievances thoroughly
    - Answer should be 50-60 words
    - Solve the actual problem presented
    - Do not invent or give unsupported facts
    - Do not make claims beyond what you know
    - Do not go beyond what the customer asks
    - Resolve the issue within 4 to 5 conversational turns

    """
    })




# Question 1
myrequest = str(input("enter your querry: "));

response1 = chat.send_message(
    f"{myrequest}"
    ,
    config={
        "response_mime_type": "application/json",
        "response_schema": ResponceModel
    }
)

print("-" * 60)

print("\nQ1:")
# print(response1.text)
chatResponceHandeler(response1);
print("\n")
print("*" * 60)






