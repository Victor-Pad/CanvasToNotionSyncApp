import requests
from config import NOTION_API_URL, NOTION_API_TOKEN, NOTION_DATABASE_ID


class NotionAPIError(Exception):
    """Exception raised for errors in the Notion API call"""
    pass