import requests
from config import CANVAS_API_URL, CANVAS_API_TOKEN
from datetime import datetime

class CanvasAPIError(Exception):
    """Exception raised for errors in the Canvas' API call"""
    pass

def make_api_requests(endpoint):
    url = f"{CANVAS_API_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {CANVAS_API_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        raise CanvasAPIError(f"Request error occurred: {err}")
