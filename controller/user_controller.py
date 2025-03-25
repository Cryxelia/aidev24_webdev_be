from flask import request
from config.db import db
from werkzeug.security import generate_password_hash


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