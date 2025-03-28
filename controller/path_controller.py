from utils.validate_types import validate_list_coords
import requests
import json
import os
from config.db import db


def generate_path(starting_point, distance_meters):
    try:
        start_coords = validate_list_coords(starting_point)
        try:
            url = "https://api.openrouteservice.org/v2/directions/foot-walking"

            payload = json.dumps(
                {
                    "coordinates": [start_coords],
                    "options": {"round_trip": {"length": distance_meters, "seed": 42}},
                }
            )
            headers = {
                "Authorization": os.getenv("OPENROUTE_API_KEY"),
                "Content-Type": "application/json",
            }

            response = requests.request(
                "POST", url, headers=headers, data=payload
            ).json()
            return response
        except Exception as e:
            return {"error": f"General error: {e}"}

    except ValueError as e:
        return {"error": f"Validation error: {e}"}


def save_path_data(path_data, user_id):
    new_path = {
        "waypoints": path_data["waypoints"],
        "title": path_data["title"],
        "distance": path_data["distance"],
        "time": path_data["time"],
        "user_id": user_id,
    }

    try:
        result = db.paths.insert_one(new_path)
        return ({"message": f"Path has been saved"}), None
    except Exception as e:
        return None, f"Database error: {str(e)}"