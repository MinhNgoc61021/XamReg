from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.student_management.excel_handling.exchange import excel_handling
from controller.student_management.student_record.student_record_management import student_record_management
from controller.log_management.log import log_management


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(log_management)
    app.register_blueprint(student_record_management)
    app.register_blueprint(authentication)
    app.register_blueprint(excel_handling)
    return app
