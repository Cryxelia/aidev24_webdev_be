from config import db

path_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["waypoints", "title", "createdAt", "user_id"],
        "properties": {
            "waypoints": {
                "bsonType": "array",
                "properties": {
                    "coordinates": {
                        "bsonType": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                            {"bsonType": "double", "minimum": -180, "maximum": 180},
                            {"bsonType": "double", "minimum": -90, "maximum": 90},
                        ],
                    }
                },
            },
            "title": {"bsonType": "string"},
            "createdAt": {"bsonType": "date"},
            "user_id": {"bsonType": "objectId"},
        },
    }
}

user_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "User Object Validation",
        "required": ["username", "password"],
        "properties": {
            "username": {
                "bsonType": "string",
            },
            "password": {
                "bsonType": "string",
            },
        },
    }
}
