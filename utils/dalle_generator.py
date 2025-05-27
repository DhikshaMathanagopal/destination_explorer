# utils/dalle_generator.py

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image_from_location(location_name):
    """
    Generate an image URL using DALL·E v3 via OpenAI Python SDK 1.x+
    """
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Beautiful landscape travel photo of {location_name}, vibrant, cinematic, HD",
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response.data[0].url
    except Exception as e:
        print(f"❌ DALL·E v3 generation failed:", e)
        return None
