from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
import re
from controller.authentication.auth import token_required
from db.entity_db import Semester_Examination, Subject_Semester, Shift, Log
from controller.time_conversion.asia_timezone import set_custom_log_time

# Log management for admin
schedule_management = Blueprint('schedule_management', __name__, url_prefix='/schedule')


@schedule_management.route('/create-new-semester', methods=['POST'])
@token_required
def add_semester(current_user):
    try:
        newSemesterTitle = request.get_json().get('newSemester')
        checkSemester = re.search('^[0-9a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶ' +
                                  'ẸẺẼỀẾỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợ' +
                                  'ụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\\s-]+$', newSemesterTitle)
        print(newSemesterTitle, flush=True)

        if checkSemester is None:
            return jsonify({'status': 'bad-request'}), 400
        else:
            newSemester = Semester_Examination.create(newSemesterTitle)
            if newSemester is False:
                return jsonify({'status': 'already-exist'}), 200
            else:
                Log.create(current_user['ID'],
                           'Tạo thêm kỳ thi ' + newSemesterTitle + ' vào hệ thống.',
                           set_custom_log_time())
                return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/remove-semester-record', methods=['DELETE'])
@token_required
def remove_semester(current_user):
    try:
        record = request.get_json()
        semID = record.get('delSemID')
        semTitle = record.get('delSemTitle')
        Semester_Examination.delRecord(semID, semTitle)
        Log.create(current_user['ID'],
                   'Xóa thông tin về kỳ thi ' + semID + ' khỏi hệ thống.',
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/semester-records', methods=['GET'])
@token_required
def get_semester(current_user):
    try:
        semesterRecords = Semester_Examination.getRecord()
        return jsonify({'status': 'success',
                        'semesterRecords': semesterRecords
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/create-subject-semester', methods=['POST'])
@token_required
def add_subject_semester(current_user):
    try:
        SubjectSemester = request.get_json()
        semID = SubjectSemester.get('semID')
        subjectID = SubjectSemester.get('subjectID')
        newSubjectSemester = Subject_Semester.create(str(subjectID), str(semID))

        if newSubjectSemester is False:
            return jsonify({'status': 'already-exist'}), 200
        else:
            Log.create(current_user['ID'],
                       'Thêm môn ' + subjectID + ' vào kỳ thi có mã ' + str(semID) + ' vào hệ thống.',
                       set_custom_log_time())
            return jsonify({'status': 'success'}), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/remove-semester-subject-record', methods=['DELETE'])
@token_required
def remove_semester_subject(current_user):
    try:
        record = request.get_json()
        semID = record.get('semID')
        subjectID = record.get('delSubjectID')
        Subject_Semester.delRecord(semID, subjectID)
        Log.create(current_user['ID'],
                   'Xóa môn thi có mã môn ' + subjectID + ' trong kỳ thi có mã ' + str(semID) + ' ra khỏi hệ thống.',
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/semester-subject-records', methods=['GET'])
@token_required
def get_semester_subject(current_user):
    try:
        semesterID = request.args.get('SemID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(semesterID, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)
        print(sort_order, flush=True)
        print(sort_field, flush=True)

        record = Subject_Semester.getRecord(semesterID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'semester_subject_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/create-new-shift', methods=['POST'])
@token_required
def add_shift(current_user):
    newShift = request.get_json()
    exam_roomID = newShift.get('RoomID')
    subjectID = newShift.get('SubjectID')
    date_start = newShift.get('Date_Start')
    start_at = newShift.get('Start_At')
    print(newShift, flush=True)
    print(subjectID, flush=True)
    print(date_start, flush=True)
    print(start_at, flush=True)
    print(exam_roomID, flush=True)
    newShift = Shift.create(subjectID, date_start, start_at, exam_roomID)
    if newShift is False:
        return jsonify({'status': 'already-exist'}), 200
    else:
        Log.create(current_user['ID'],
                   'Thêm ca thi mới vào môn thi có mã ' + str(subjectID) + ' trong hệ thống.',
                   set_custom_log_time())
        return jsonify({'status': 'success'}), 200


@schedule_management.route('/shift-records', methods=['GET'])
@token_required
def get_shift(current_user):
    try:
        subjectID = request.args.get('subjectID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(subjectID, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)
        print(sort_order, flush=True)
        print(sort_field, flush=True)

        record = Shift.getRecord(subjectID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'shift_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/remove-shift-record', methods=['DELETE'])
@token_required
def remove_shift(current_user):
    try:
        record = request.get_json()
        delShiftID = record.get('delShiftID')
        currentSubjectID = record.get('currentSubjectID')
        print(delShiftID, flush=True)
        print(currentSubjectID, flush=True)
        Shift.delRecord(str(delShiftID))
        Log.create(current_user['ID'],
                   'Xóa ca thi có mã số ' + str(delShiftID) + ' trong môn thi có mã ' +
                       currentSubjectID + ' ra khỏi hệ thống.',
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400
