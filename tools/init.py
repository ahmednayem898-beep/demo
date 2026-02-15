import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Please set your OPENROUTER_API_KEY in .env file")
