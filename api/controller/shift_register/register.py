from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import Student_Shift

# shift register for student
shift_register = Blueprint('shift_register', __name__, url_prefix='/shift-register')


@shift_register.route('/add-student-shift', methods=['POST'])
@token_required
def add_student_shift(current_user):
    StudentID = request.get_json().get('StudentID')
    ShiftID = request.get_json().get('newFullname')
    print(StudentID, flush=True)
    print(ShiftID, flush=True)


