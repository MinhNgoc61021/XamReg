from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from controller.time_conversion.asia_timezone import set_custom_log_time
from db.entity_db import Subject, Log
import re

subject_management = Blueprint('subject_management', __name__, url_prefix='/subject')


@subject_management.route('/subject-records', methods=['GET'])
@token_required
def get_subject_record(current_user):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_field = request.args.get('sort_field')
        sort_order = request.args.get('sort_order')
        record = Subject.getSubjectRecord(page_index, per_page, sort_field, sort_order)

        return jsonify({
            'status': 'success',
            'records': record[0],
            'page_number': record[1].page_number,
            'page_size': record[1].page_size,
            'num_pages': record[1].num_pages,
            'total_results': record[1].total_results
        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@subject_management.route('/create-subject', methods=['POST'])
@token_required
def create_subject(current_user):
    try:
        newSubjectID = request.get_json().get('SubjectID')
        newSubjectTitle = request.get_json().get('SubjectTitle')
        print(newSubjectID, flush=True)
        print(newSubjectTitle, flush=True)
        validateSubjectID = re.search('(^(([A-Z]|[a-z]){3})([1-9][(0-9)]{3})$)', str(newSubjectID))
        validateSubjectTitle = re.search("^[a-zA-Z1-9_"
                                         "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-–\s()& ]+$", newSubjectTitle)
        if validateSubjectID is not None or validateSubjectTitle is not None:
            isNew = Subject.create(str(newSubjectID).upper().strip(), newSubjectTitle)
            if isNew:
                Log.create(current_user['ID'],
                           'Thêm môn học: ' + str(newSubjectID).upper().strip() + ' ' + newSubjectTitle + 'vào hệ '
                                                                                                          'thống.',
                           set_custom_log_time())
                return jsonify({'status': 'success'}), 200
            else:
                return jsonify({'status': 'already-exist'}), 202
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@subject_management.route('/edit-subject', methods=['put'])
@token_required
def edit_subject(current_user):
    try:
        currentSubjectID = request.get_json().get('currentSubjectID')
        newSubjectID = request.get_json().get('SubjectID')
        newSubjectTitle = request.get_json().get('SubjectTitle')
        print(newSubjectID, flush=True)
        print(newSubjectTitle, flush=True)
        validateSubjectID = re.search('(^(([A-Z]|[a-z]){3})([1-9][(0-9)]{3})$)', str(newSubjectID).strip())
        validateSubjectTitle = re.search("^[a-zA-Z1-9_"
                                         "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\-–\s()& ]+$", newSubjectTitle)
        print(validateSubjectID, flush=True)
        if validateSubjectID is not None or validateSubjectTitle is not None:
            success = Subject.updateRecord(currentSubjectID, str(newSubjectID).upper().strip(),
                                           str(newSubjectTitle).strip())
            if success is True:
                Log.create(current_user['ID'],
                           'Thay đổi thông tin môn học: ' + currentSubjectID + ' thành ' + str(
                               newSubjectID).upper().strip() + ' | ' + newSubjectTitle,
                           set_custom_log_time())
                return jsonify({'status': 'success'}), 200
            else:
                return jsonify({'status': 'already-exist'}), 202
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@subject_management.route('/remove-subject', methods=['delete'])
@token_required
def remove_subject(current_user):
    try:
        delSubjectID = request.get_json().get('delSubjectID')
        validate = re.search('(^(([A-Z]|[a-z]){3})([1-9][(0-9)]{3})$)', str(delSubjectID))
        if validate:
            Subject.delRecord(delSubjectID)
            Log.create(current_user['ID'],
                       'Xóa môn học: ' + delSubjectID + ' khỏi hệ thống.',
                       set_custom_log_time())
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@subject_management.route('search-subject', methods=['GET'])
@token_required
def search_subject(current_user):
    try:
        searchID = request.args.get('searchID')
        search_results = Subject.searchSubjectRecord(searchID)
        return jsonify({'status': 'success',
                        'search_results': search_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400
