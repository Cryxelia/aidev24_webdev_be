from flask import request
from config.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from controller.auth_controller import generate_jwt


def create_user(username, password):
    existing_user = db.users.find_one({"username" : username})
    if existing_user:
        return None, "User already exists"
    
    hashed_pw = generate_password_hash(password)
    new_user ={
        "username" : username,
        "password" : hashed_pw
    }

    try:
        result = db.users.insert_one(new_user) 
        return {"id": str(result.inserted_id), "username": username}, None  
    except Exception as e:
        return None, f"Database error: {str(e)}"
    
    

def delete_user(username):

    result = db.users.delete_one({"username": username})

    if result.deleted_count == 0:
        return ({"error": "User not found"})

    return ({"message": f"User '{username}' has been deleted"})
def show_user(username):
    user = db.users.find_one({"username": username})
    if not user:
        return None, "user not found"
    
    if user:
        return {"username": user["username"]}
    
def show_all_users():
    users = db.users.find()
    user_list = []
    for user in users:
        user_list.append({"username": user["username"]})

    return user_list

def login_user(username, password):
    user = db.users.find_one({"username": username}) 

    if not user or not check_password_hash(user["password"], password):
        return None, "Invalid username or password"
    
    token = generate_jwt({"user_id": user["_id"], "username": user["username"]})

    return {"username": user["username"], "token": token}, None

def update_username_by_id(user_id, new_username):
    from bson.objectid import ObjectId

    try:
        _id = ObjectId(user_id)
    except:
        return None, "Invalid user ID format"

    user = db.users.find_one({"_id": _id})

    if not user:
        return None, "User not found"

    if user["username"] == new_username:
        return None, "The new username is the same as the existing one"

    username_check = db.users.find_one({"username": new_username, "_id": {"$ne": _id}})

    if username_check:
        return None, "That username is taken by another user"

    result = db.users.update_one({"_id": _id}, {"$set": {"username": new_username}})

    if result.modified_count == 0:
        return None, "Failed to update username"

    updated_user = db.users.find_one({"_id": _id})
    if not updated_user:
        return None, "Failed to retrieve updated user"

    return {"user_id": str(_id), "username": updated_user["username"]}, None

def show_all_user_paths(user_id):
    try:
        user_paths = db.paths.find({"user_id": user_id})
        path_list = []
        for path in user_paths:
            path_list.append({
                "waypoints": path["waypoints"],
                "title": path["title"],
                "distance": path["distance"],
                "time": path["time"]
            })

        return path_list if path_list else None
    except Exception as e:
        print(f"Error fetching user paths: {e}")
        return None