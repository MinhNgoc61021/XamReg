from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import User, Subject
import re

subjects_management = Blueprint('subjects_management', __name__, url_prefix='/record')

@subjects_management.route('/subjects-record', method = ["GET"])
@token_required
def get_subject_record(subject):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')
        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        record = Subject.getRecord(page_index, per_page, sort_field, sort_order)
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