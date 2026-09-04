from dotenv import load_dotenv
import os 
from google import genai
from pydantic import BaseModel
from typing import Literal
from generateText import chatResponceHandeler
from ask_llm import ask_llmAI


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

def main():
    chat = ask_llmAI(client);
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


if __name__ == "__main__":
    main()






