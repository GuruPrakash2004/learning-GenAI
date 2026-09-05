from dotenv import load_dotenv
import os 
from google import genai
from generateText import chatResponceHandeler
from ask_llm import AI_ChatHandeler
from responceData import responceData
import asyncio


load_dotenv()

async def main():
# get the key from env
    api_key = os.getenv("GEMINI_API_KEY")
# create the client 
    client = genai.Client(api_key=api_key);
# create chat for state maintain
    chat = AI_ChatHandeler(client);
    # Question input
    myinput = str(input("enter your querry: "));

    response1 =await  responceData(chat,myinput)

    print("-" * 60)
    print("\nQ1:")
    chatResponceHandeler(response1);
    print("\n")
    print("*" * 60)


if __name__ == "__main__":
    asyncio.run(main())






