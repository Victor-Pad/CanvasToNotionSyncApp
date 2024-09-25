import requests
from config import CANVAS_API_URL, CANVAS_API_TOKEN
from datetime import datetime

class CanvasAPIError(Exception):
    """Exception raised for errors in the Canvas' API call"""
    pass

