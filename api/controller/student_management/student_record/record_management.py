from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import User

record_management = Blueprint('record_management', __name__, url_prefix='/record')


@record_management.route('/student-records', methods=['GET'])
@token_required
def get_student_record(current_user):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')
        print(sort_order, flush=True)
        print(sort_field, flush=True)
        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        record = User.getRecord(page_index, per_page, sort_field, sort_order)
        print(record[1], flush=True)

        return jsonify({'status': 'success',
                        'records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@record_management.route('/remove-record', methods=['DELETE'])
@token_required
def remove_record(current_user):
    try:
        # print(request.get_json('studentID'), flush=True)
        record = request.get_json()
        studentID = record.get('studentID')
        User.delRecord(str(studentID))
        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400
