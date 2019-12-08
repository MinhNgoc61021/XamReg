from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import Log
import re

log_management = Blueprint('log_management', __name__, url_prefix='/log')


@log_management.route('/log-records', methods=['GET'])
@token_required
def get_log_records(current_user):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        log_record = Log.getLog(page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'log_records': log_record[0],
                        'page_number': log_record[1].page_number,
                        'page_size': log_record[1].page_size,
                        'num_pages': log_record[1].num_pages,
                        'total_results': log_record[1].total_results,
                        }), 200

    except:
        return jsonify({'status': 'bad-request'}), 400
