from utils.validate_types import validate_list_coords
import requests
import json
import os

def generate_route(starting_point, distance_meters):
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

            response = requests.request("POST", url, headers=headers, data=payload).json()
            return response
        except Exception as e:
            return {"error": f"General error: {e}"}

    except ValueError as e:
        return {"error": f"Validation error: {e}"}
