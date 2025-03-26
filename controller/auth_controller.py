import jwt
import datetime
import os

def generate_jwt(user):
  
  payload = {
    "username": user["username"],
    "expiration": (datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)).isoformat()
  }
  token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")
  
  return token

def authenticate_jwt(encoded_token):
  decoded_token = jwt.decode(encoded_token, os.getenv("SECRET_KEY"), algorithms="HS256")
  token_expiration = datetime.datetime.fromisoformat(decoded_token["expiration"])
  current_timestamp = datetime.datetime.now(datetime.UTC)
  
  if current_timestamp > token_expiration:
    return {"error": "Token expired"}
  else:
    return decoded_token
  
