from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
import re
from controller.authentication.auth import token_required
from db.entity_db import Semester_Examination, Room_Shift, Shift, Log
from controller.time_conversion.asia_timezone import set_custom_log_time

# Log management for admin
schedule_management = Blueprint('schedule_management', __name__, url_prefix='/schedule')


@schedule_management.route('/create-semester', methods=['POST'])
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


@schedule_management.route('/remove-semester', methods=['DELETE'])
@token_required
def remove_semester(current_user):
    try:
        record = request.get_json()
        semID = record.get('delSemID')
        semTitle = record.get('delSemTitle')
        Semester_Examination.delRecord(semID, semTitle)
        Log.create(current_user['ID'],
                   'Xóa thông tin về kỳ thi ' + str(semID) + ' khỏi hệ thống.',
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


@schedule_management.route('/create-shift', methods=['POST'])
@token_required
def create_shift(current_user):
    try:
        shift = request.get_json()
        semID = shift.get('semID')
        subjectID = shift.get('subjectID')
        date_start = shift.get('date_start')
        start_at = shift.get('start_at')
        end_at = shift.get('end_at')
        newShift = Shift.create(str(subjectID),
                                str(semID),
                                date_start,
                                start_at,
                                end_at)

        if newShift is False:
            return jsonify({'status': 'already-exist'}), 200
        else:
            Log.create(current_user['ID'],
                       'Thêm ca thi vào kỳ thi có mã ' + str(semID) + ' vào hệ thống.',
                       set_custom_log_time())
            return jsonify({'status': 'success'}), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/remove-shift', methods=['DELETE'])
@token_required
def remove_shift(current_user):
    try:
        record = request.get_json()
        shiftID = record.get('delShiftID')
        Shift.delRecord(shiftID)
        Log.create(current_user['ID'],
                   'Xoá ca thi có mã ' + str(shiftID) + ' ra khỏi hệ thống.',
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/shift-records', methods=['GET'])
@token_required
def get_shift(current_user):
    try:
        semesterID = request.args.get('semID')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(semesterID, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)
        print(sort_order, flush=True)
        print(sort_field, flush=True)

        record = Shift.getRecord(semesterID, page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'shift_records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


#
# @schedule_management.route('/update-shift' , methods=['PUT'])
# @token_required
# def update_shift:
#

@schedule_management.route('/create-room', methods=['POST'])
@token_required
def create_room(current_user):
    try:
        room_shift = request.get_json()
        shiftID = room_shift.get('shiftID')
        roomID = room_shift.get('roomID')
        print(shiftID, flush=True)
        print(roomID, flush=True)
        newRoomShift = Room_Shift.create(roomID,
                                         shiftID)

        if newRoomShift is False:
            return jsonify({'status': 'already-exist'}), 200
        else:
            Log.create(current_user['ID'],
                       'Thêm phòng thi có mã ' + str(roomID) + ' vào ca thi ' + str(shiftID) + ' vào hệ thống.',
                       set_custom_log_time())
            return jsonify({'status': 'success'}), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/remove-room', methods=['DELETE'])
@token_required
def remove_room(current_user):
    try:
        record = request.get_json()
        shiftID = record.get('delShiftID')
        Room_Shift.delRecord(shiftID)
        Log.create(current_user['ID'],
                   'Xoá phòng thi có mã ' + str(shiftID) + ' ra khỏi hệ thống.',
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@schedule_management.route('/room-records', methods=['GET'])
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
