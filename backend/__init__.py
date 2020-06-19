from flask import Flask, jsonify
from flask_cors import CORS
from backend.routes import api


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app)
    flask_app.register_blueprint(api)
    return flask_app
