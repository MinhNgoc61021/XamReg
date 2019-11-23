from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.student_management.excel_handling.exchange import excel_handling
from controller.student_management.student_record.record_management import record_management

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(record_management)
    app.register_blueprint(authentication)
    app.register_blueprint(excel_handling)
    return app
