import requests
from typing import Optional

API_URL = "https://rickandmortyapi.com/api/character"

def fetch_characters(page=1) -> Optional[dict]:
    try:
        response = requests.get(f"{API_URL}?page={page}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from Rick and Morty API: {e}")
        return None

