import re

from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import Shift, Semester_Examination, Room_Shift

# shift register for student
shift_register = Blueprint('shift_register', __name__, url_prefix='/shift-register')


@shift_register.route('/add-student-shift', methods=['POST'])
@token_required
def add_student_shift(current_user):
    StudentID = request.get_json().get('StudentID')
    ShiftID = request.get_json().get('newFullname')
    print(StudentID, flush=True)
    print(ShiftID, flush=True)


@shift_register.route('/shift-records', methods=['get'])
@token_required
def get_shift(current_user):
    try:
        SemID = request.args.get('SemID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        record = Shift.getQualifiedShiftRecord(SemID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'shift_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@shift_register.route('/search-semester', methods=['get'])
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


@shift_register.route('/room-records', methods=['GET'])
@token_required
def get_room(current_user):
    try:
        shiftID = request.args.get('shiftID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(shiftID, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)
        print(sort_order, flush=True)
        print(sort_field, flush=True)

        record = Room_Shift.getRecord(shiftID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'room_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400
