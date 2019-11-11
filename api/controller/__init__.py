from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.test.test import tester
from controller.authentication.auth import *

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(authentication)
    app.register_blueprint(tester)
    return app
