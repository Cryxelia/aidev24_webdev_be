from controller.user_controller import create_user, show_user, show_all_users, login_user, delete_user
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

@user_routes.route("/delete-user", methods=["DELETE"])
def delete_user(username):
    user_data = request.get_json()
    if not user_data or "username" not in user_data:
        return jsonify({"error": "Missing username or password"}), 400
    if delete_user(username):
        return jsonify({"message": f"User '{username}' has been deleted"}), 200

    return jsonify({"error": "User not found"}), 404



@user_routes.route("/show-user", methods=["GET"])
def get_user():

    user_data = request.get_json()

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Missing username"}), 400

    user_info = show_user(user_data["username"])

    print(user_info)

    if not user_info:
        return jsonify({"error": "User not found"}), 404

    return jsonify({'user': user_info}), 200

@user_routes.route("/show-all-users", methods=["GET"])
def get_all_users():
    return jsonify({'users': show_all_users()}), 200


@user_routes.route("/login", methods=["POST"])
def login():
    user_data = request.get_json()

    if not user_data or "username" not in user_data or "password" not in user_data:
        return jsonify({"error": "Missing username or password"}), 400

    user_info, error = login_user(user_data["username"], user_data["password"])

    if error:
        return jsonify({"error": error}), 401

    return jsonify({'message': 'User logged in successfully', 'user': user_info}), 200
