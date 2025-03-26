from flask import request
from config.db import db
from werkzeug.security import generate_password_hash, check_password_hash


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

    return {"username": user["username"]}, None
