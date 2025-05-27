import os
from dotenv import load_dotenv

load_dotenv()

print("✅ Loaded:", os.getenv("OPENAI_API_KEY"))