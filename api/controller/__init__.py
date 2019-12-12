from flask import Flask
from flask_cors import CORS
from controller.authentication.auth import authentication
from controller.student_management.excel_handling.exchange import excel_handling
from controller.student_management.student_record.student_record_management import student_record_management
from controller.subject_management.subject_management import subject_management
from controller.log_management.log import log_management
from controller.shift_register.register import shift_register
from controller.schedule_management.schedule_management import schedule_management
from controller.exam_room_management.exam_room_management import exam_room_management


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(log_management)
    app.register_blueprint(student_record_management)
    app.register_blueprint(schedule_management)
    app.register_blueprint(authentication)
    app.register_blueprint(excel_handling)
    app.register_blueprint(subject_management)
    app.register_blueprint(shift_register)
    app.register_blueprint(subject_management)
    app.register_blueprint(exam_room_management)
    return app
