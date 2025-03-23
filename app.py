from flask import Flask
from dotenv import load_dotenv
import os
from routes.user_route import user_routes


load_dotenv()

app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix='/users')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)