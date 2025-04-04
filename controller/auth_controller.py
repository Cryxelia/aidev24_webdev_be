import jwt
import datetime
import os
from config.db import db

def generate_jwt(user):
    payload = {
        "user_id": str(user["user_id"]),
        "username": user["username"],
        "expiration": (
            datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)
        ).isoformat(),
    }
    
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")

    return token


def authenticate_jwt(token):
    if not token:
        return {"error": "Token is missing"}

    try:
        if isinstance(token, str):
            token = token.encode("utf-8")
    
        decoded_token = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])

        token_expiration = datetime.datetime.fromisoformat(decoded_token["expiration"])
        current_timestamp = datetime.datetime.now(datetime.UTC)

        if current_timestamp > token_expiration:
            return {"error": "Token expired"}
        else:
            return decoded_token

    except jwt.DecodeError as e:
        return {"error": f"Invalid token: {str(e)}"}
    except Exception as e:
        return {"error": f"Authentication error: {str(e)}"}
