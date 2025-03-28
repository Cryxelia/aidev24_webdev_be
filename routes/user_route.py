from controller.user_controller import create_user, show_user, show_all_users, login_user, delete_user, update_username_by_id
from controller.auth_controller import authenticate_jwt
from flask import Blueprint, jsonify, request, make_response

user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/create-user", methods=["POST"])
def new_user():
    user_data = request.get_json()

    if not user_data or "username" not in user_data or "password" not in user_data:
        return jsonify({"error": "Missing username or password"}), 400
    
    new_user, error = create_user(user_data["username"], user_data["password"])

    if error:
        return jsonify({'error': error}), 400  

    return jsonify({'message': 'User created successfully'}), 201 

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

    response = make_response(jsonify({'message': 'User logged in successfully', 'user': user_info}), 200)
    response.set_cookie("token", user_info["token"], httponly=True, secure=True, samesite="Strict")
    return response

@user_routes.route("/update-user", methods=["POST"])
def update_user():

    token = authenticate_jwt(request.cookies.get("token"))
    user_id = token["user_id"]

    user_data = request.get_json()
    
    if not user_data or "new_username" not in user_data:
        return jsonify({"error": "Missing new username"}), 400
    
    result, error = update_username_by_id(user_id=user_id, new_username=user_data["new_username"])
    
    if error:
        return jsonify({"error": error})
    
    return jsonify({'message': 'User updated successfully', "user": result}), 200

@user_routes.route("/logout", methods=["POST"])
def logout():
    response = make_response(jsonify({'message': 'User has logged out'}), 200)
    response.set_cookie('token', '', expires=0, httponly=True, path='/')
    return response