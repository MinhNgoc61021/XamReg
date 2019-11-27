from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from db.entity_db import User, Subject, Student_Status
from controller.authentication.auth import token_required
import re
from flask_sqlalchemy import BaseQuery

record_management = Blueprint('record_management', __name__, url_prefix='/record')


@record_management.route('/get_user/<int:page_num>', methods=['GET'])
def get_student_record(page_num):
    record = BaseQuery(User).paginate(page=page_num, per_page=5, error_out=True)
    return record.items
