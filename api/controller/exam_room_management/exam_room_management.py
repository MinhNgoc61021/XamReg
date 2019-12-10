from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import User, Subject, Exam_Room, Shift, Exam_Room_Cache
import re

exam_room_management = Blueprint('exam_room_management', __name__, url_prefix='/room')

@exam_room_management.route('/room-cache-records', methods=['GET'])
@token_required
def get_room_cache_record(current_room):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')
        # print(sort_order, flush=True)
        # print(sort_field, flush=True)
        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        record = Exam_Room_Cache.getRecord_cache(page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200

    except:
        return jsonify({'status': 'bad-request'}), 400