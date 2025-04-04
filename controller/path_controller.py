from utils.validate_types import validate_list_coords
import requests
import json
import os
from config.db import db
from random import randint
from bson import ObjectId  

def generate_path(starting_point, distance_meters):
    try:
        start_coords = validate_list_coords(starting_point)
        try:
            url = "https://api.openrouteservice.org/v2/directions/foot-walking"

            randomize_seed = randint(1, 42)

            payload = json.dumps(
                {
                    "coordinates": [start_coords],
                    "options": {
                        "round_trip": {
                            "length": distance_meters,
                            "seed": randomize_seed,
                        }
                    },
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
        return ({"message": "Path has been saved"}), None
    except Exception as e:
        return None, f"Database error: {str(e)}"


def delete_path_by_id(path_id):
    try:
        object_id = ObjectId(path_id)
    except Exception as e:
        return {"error": f"Invalid path_id format: {e}"}

    try:
        result = db.paths.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            return None, "Path not found"
        return {"message": "Path has been deleted"}, None
    except Exception as e:
        return None, f"Database error: {str(e)}"


def update_path_by_id(path_id, pathData):
    try:
        path_id = ObjectId(path_id)
    except Exception as e:
        return {"error": f"Invalid path_id format: {e}"}

    path = db.paths.find_one({"_id": path_id})

    waypoints = pathData.get("waypoints")
    title = pathData.get("title")
    distance = pathData.get("distance")
    time = pathData.get("time")

    if not path:
        return None, "Path not found"

    result = db.paths.update_one(
        {"_id": path_id},
        {
            "$set": {
                "waypoints": waypoints,
                "title": title,
                "distance": distance,
                "time": time,
            }
        },
    )

    if result.modified_count == 0:
        return None, "Failed to update path"

    return {"message": "Path has been updated"}, None
