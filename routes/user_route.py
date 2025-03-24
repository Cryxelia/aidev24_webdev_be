from controller.user_controller import create_user
from flask import Blueprint, jsonify, request


user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/create-user", methods=["POST"])
def new_user():
    user_data = request.get_json()

    if not user_data or "username" not in user_data or "password" not in user_data:
        return jsonify({"error": "Missing username or password"}), 400
    
    new_user, error = create_user(user_data["username"], user_data["password"])

    if error:
        return jsonify({'error': error}), 400  

    return jsonify({'message': 'User created successfully', 'user': new_user}), 201 