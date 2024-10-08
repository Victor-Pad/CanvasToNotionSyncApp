import requests
from config import CANVAS_API_URL, CANVAS_API_TOKEN


class CanvasAPIError(Exception):
    """Exception raised for errors in the Canvas' API call"""
    pass

def make_api_request(endpoint):
    url = f"{CANVAS_API_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {CANVAS_API_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        raise CanvasAPIError(f"Request error occurred: {err}")


def get_assignments(course_id):
    """Get assignments for a course"""
    return make_api_request(f"/courses/{course_id}/assignments")


def get_course_code(course_id):
    """Get the course code for a course."""
    course_data = make_api_request(f"/courses/{course_id}")
    return course_data.get("course_code", "Unknown")
