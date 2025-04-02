from flask import Flask
from dotenv import load_dotenv
from routes.user_route import user_routes
from routes.path_route import path_routes
from flask_cors import CORS
import os

def create_app(test_config=None):
    """Application factory to create and configure the Flask app."""
    load_dotenv()

    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    CORS(app, supports_credentials=True)

    
    app.register_blueprint(user_routes, url_prefix="/users")
    app.register_blueprint(path_routes, url_prefix="/paths")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
