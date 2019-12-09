from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.student_management.excel_handling.exchange import excel_handling
from controller.log_management.log import log_management
from controller.student_management.student_record.record_management import record_management
from controller.subjects_management.subjects_management import subjects_management

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(log_management)
    app.register_blueprint(student_record_management)
    app.register_blueprint(authentication)
    app.register_blueprint(excel_handling)
    app.register_blueprint(subjects_management)
    return app
