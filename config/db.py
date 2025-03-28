import os
from pymongo import MongoClient
from dotenv import load_dotenv
from schemas.schemas import user_schema, path_schema

load_dotenv()

connection_string = f"{os.getenv('MONGODB_URI')}"

client = MongoClient(connection_string)

db = client[os.getenv("MONGODB_DB")]


def create_user_collection():
    try:
        db.create_collection("users")
    except Exception as e:
        print(e)
    db.command("collMod", "users", validator=user_schema,validationAction="error")


def create_path_collection():
    try:
        db.create_collection("paths")
    except Exception as e:
        print(e)
    db.command("collMod", "paths")


create_user_collection()
create_path_collection()
