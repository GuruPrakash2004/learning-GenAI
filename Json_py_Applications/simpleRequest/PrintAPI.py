import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GitHub_API");

print(api_key);