from controller.path_controller import generate_route
from flask import Blueprint, jsonify, request
from utils.polyline import decode_polyline
path_routes = Blueprint('path_routes', __name__)

@path_routes.route("/get-path", methods=["GET"])
def get_path():
    request_payload = request.get_json()
    print(request_payload)

    if not request_payload or "starting_point" not in request_payload or "distance" not in request_payload:
        return jsonify({"error": "Missing either starting_point or distance"}), 400

    path_data = generate_route(starting_point=request_payload["starting_point"], distance_meters=request_payload["distance"])

    encoded_polyline = path_data["routes"][0]["geometry"]
    decoded_polyline = decode_polyline(encoded_polyline)
    
    return jsonify({'path': decoded_polyline}), 200