from controller.user_controller import create_user, show_user, show_all_users, login_user, delete_user_by_id, update_username_by_id, show_all_user_paths, update_password, get_user_path
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
def delete_user():
    token = authenticate_jwt(request.cookies.get("token"))
    user_id = token["user_id"]

    if delete_user_by_id(user_id):
        return jsonify({"message": f"User '{user_id}' has been deleted"}), 200

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

@user_routes.route("/update-user", methods=["PUT"])
def update_user():

    token = authenticate_jwt(request.cookies.get("token"))
    user_id = token["user_id"]

    user_data = request.get_json()
    
    if not user_data or "new_username" not in user_data:
        return jsonify({"error": "Missing new username"}), 400
    
    result, error = update_username_by_id(user_id=user_id, new_username=user_data["new_username"])
    
    if error:
        return jsonify({"error": error}), 400
    
    return jsonify({'message': 'User updated successfully', "user": result}), 201

@user_routes.route("/update-user-password", methods=["PUT"])
def update_user_password():

    token = authenticate_jwt(request.cookies.get("token"))
    user_id = token["user_id"]

    user_data = request.get_json()
    
    if not user_data or "new_password" not in user_data or "old_password" not in user_data or "confirm_password" not in user_data:
        return jsonify({"error": "Missing new password, old password or confirm password"}), 400
    
    result, error = update_password(user_id, old_password = user_data["old_password"], new_password = user_data["new_password"], confirm_password = user_data["confirm_password"])

    if error:
        return jsonify({"error": error}), 400
    
    return jsonify({'message': 'User password updated successfully', "user": result}), 201


@user_routes.route("/logout", methods=["POST"])
def logout():
    response = make_response(jsonify({'message': 'User has logged out'}), 200)
    response.set_cookie('token', '', expires=0, httponly=True, path='/')
    return response

@user_routes.route("/get-paths", methods=["GET"])
def get_user_paths():
    token = authenticate_jwt(request.cookies.get("token"))
    if not token["user_id"]:
        return jsonify({"error": "Token validation error"}), 400

    user_id = token["user_id"]
    paths = show_all_user_paths(user_id)

    return jsonify({"paths": paths}), 200

@user_routes.route("/get-path", methods=["GET"])
def get_path():
    token = authenticate_jwt(request.cookies.get("token"))
    if not token["user_id"]:
        return jsonify({"error": "Token validation error"}), 400
    
    user_id = token["user_id"]
    path, error = get_user_path(user_id)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"path": path}), 200