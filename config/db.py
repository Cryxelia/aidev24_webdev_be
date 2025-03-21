import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_string = f"{os.getenv('MONGODB_URI')}"

client = MongoClient(connection_string)

db = client[os.getenv('MONGODB_DB')]