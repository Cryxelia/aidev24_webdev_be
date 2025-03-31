from flask import Flask
from dotenv import load_dotenv
from routes.user_route import user_routes
from routes.path_route import path_routes
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(user_routes, url_prefix="/users")
app.register_blueprint(path_routes, url_prefix="/paths")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)