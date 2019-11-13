from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.authentication.auth import *
from controller.student_management.excel_handling.exchange import excel_handling

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(authentication)
    app.register_blueprint(excel_handling)
    return app
