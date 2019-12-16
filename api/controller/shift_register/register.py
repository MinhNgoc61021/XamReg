import re

from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import Shift, Semester_Examination, Room_Shift, Student_Shift, Log
from controller.time_conversion.asia_timezone import set_custom_log_time

# shift register for student
shift_register = Blueprint('shift_register', __name__, url_prefix='/shift-register')


@shift_register.route('/shift-records', methods=['GET'])
@token_required
def get_shift(current_user):
    try:
        SemID = request.args.get('SemID')
        StudentID = request.args.get('StudentID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(SemID, flush=True)
        print(StudentID, flush=True)
        print(per_page, flush=True)

        record = Shift.getQualifiedShiftRecord(SemID, StudentID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'shift_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/search-subject', methods=['get'])
@token_required
def search_subject(current_user):
    try:
        searchID = request.args.get('searchID')
        validatesearchID = re.search('[!#$%^&*()='',.?":{}|<>]', str(searchID))
        if validatesearchID is None:
            search_results = Shift.searchShiftRecord(searchID)
            return jsonify({'status': 'success',
                            'search_results': search_results,
                            }), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/search-semester', methods=['GET'])
@token_required
def search_semester(current_user):
    try:
        searchID = request.args.get('searchID')
        validatesearchID = re.search('[!#$%^&*()='',.?":{}|<>]', str(searchID))
        if validatesearchID is None:
            search_results = Semester_Examination.searchSemesterRecord(searchID)
            return jsonify({'status': 'success',
                            'search_results': search_results,
                            }), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/room-records', methods=['GET'])
@token_required
def get_room(current_user):
    shiftID = request.args.get('shiftID')
    studentID = request.args.get('studentID')
    page_index = request.args.get('page_index')
    per_page = request.args.get('per_page')
    sort_order = request.args.get('sort_order')
    sort_field = request.args.get('sort_field')

    print(shiftID, flush=True)
    print(page_index, flush=True)
    print(per_page, flush=True)
    print(sort_order, flush=True)
    print(sort_field, flush=True)

    record = Room_Shift.getRegisterRoom(shiftID, page_index, per_page, sort_field, sort_order)

    return jsonify({'status': 'success',
                    'room_records': record[0],
                    'page_number': record[1].page_number,
                    'page_size': record[1].page_size,
                    'num_pages': record[1].num_pages,
                    'total_results': record[1].total_results,
                    }), 200


@shift_register.route('/unregister-shift', methods=['delete'])
@token_required
def unregister_shift(current_user):
    try:
        studentID = request.args.get('studentID')
        Room_ShiftID = request.args.get('Room_ShiftID')
        Student_Shift.delRecord(studentID,  Room_ShiftID)
        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/register-shift', methods=['POST'])
@token_required
def register_shift(current_user):
    try:
        studentID = request.get_json().get('studentID')
        Room_ShiftID = request.get_json().get('Room_ShiftID')
        check = Student_Shift.create(Room_ShiftID, studentID)
        if check is False:
            return jsonify({'status': 'already-exist'}), 200
        else:
            Log.create(current_user['ID'],
                       'Đã đăng ký ca thi ' + str(Room_ShiftID),
                       set_custom_log_time())
            return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/registered-room-shift-records', methods=['GET'])
@token_required
def get_registered_room_shift(current_user):
    try:
        studentID = request.args.get('studentID')


        # Gọi về backend
        record = Student_Shift.getRegisteredRoom_Shift(studentID)

        return jsonify({'status': 'success',
                        'room_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/registered-shift-records', methods=['get'])
@token_required
def get_registered_shift(current_user):
    try:
        studentID = request.args.get('student')
        SemID = request.args.get('SemID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        # query ở đây
        record = Shift.getQualifiedShiftRecord(SemID, studentID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'shift_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400
