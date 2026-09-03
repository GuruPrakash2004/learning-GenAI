import os
from dotenv import load_dotenv


load_dotenv()

def main():
    my_Api = os.getenv("AI_API_KEY");
    print(my_Api)

main()


