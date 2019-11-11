from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.authentication.auth import *

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(authentication)
    return app
