import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "your-secret-key")
API_KEY_NAME = "X-API-Key"
