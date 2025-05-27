# config.py
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "your_password",
    "database": "Travel"
}
