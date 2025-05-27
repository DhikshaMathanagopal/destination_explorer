import requests
from config import GOOGLE_API_KEY, GOOGLE_CX

def fetch_image_url(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'cx': GOOGLE_CX,
        'key': GOOGLE_API_KEY,
        'searchType': 'image',
        'num': 1,
        'safe': 'high'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json().get("items")
        if items:
            return items[0]["link"]
    return None
