from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import User, Subject, Exam_Room, Log
from controller.time_conversion.asia_timezone import set_custom_log_time
import re

exam_room_management = Blueprint('exam_room_management', __name__, url_prefix='/room')

@exam_room_management.route('/create-room-records', methods=['POST'])
@token_required
def create_room_record(current_user):
    try:
        newRoomName = request.get_json().get('newRoomName')
        newMaxcapacity = request.get_json().get('newMaxcapacity')

        print(newRoomName, flush=True)
        print(newMaxcapacity, flush=True)

        Log.create(current_user['ID'],
                   'Tạo thêm phòng thi ' + newRoomName,
                   set_custom_log_time())

        newRoom = Exam_Room.create(newRoomName, newMaxcapacity)
        if newRoom is False:
            return jsonify({'status': 'already-exist'}), 200
        else:
            return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400

@exam_room_management.route('/room-records', methods=['GET'])
@token_required
def get_room_record(current_user):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')
        print(sort_order, flush=True)
        print(sort_field, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)

        record = Exam_Room.getRecord(page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200


    except:
        return jsonify({'status': 'bad-request'}), 400


@exam_room_management.route('/update-room-record', methods=['PUT'])
@token_required
def update_room_record(current_user):
    try:
        new_update = request.get_json()
        currentRoomID = new_update.get('currentRoomID')
        newRoomID = new_update.get('RoomID')
        newRoomName = new_update.get('RoomName')
        newMaxcapacity = new_update.get('Maxcapacity')

        # print(currentStudentID, flush=True)
        # print(newStudentID, flush=True)
        # print(newUsername, flush=True)
        # print(newFullname, flush=True)

        Exam_Room.updateRecord(currentRoomID, newRoomID, newRoomName, newMaxcapacity)
        Log.create(current_user['ID'],
                   'Cập nhật thông tin của phòng thi ' + newRoomName,
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@exam_room_management.route('/remove-room-record', methods=['DELETE'])
@token_required
def remove_room_record(current_user):
    try:
        # print(request.get_json('studentID'), flush=True)
        record = request.get_json()
        roomID = record.get('delRoomID')
        roomName = record.get('delRoomName')

        Exam_Room.delRecord(str(roomID))
        Log.create(current_user['ID'],
                   'Xóa phòng thi ' + roomName + ".",
                   set_custom_log_time())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400

@exam_room_management.route('/search-room-record', methods=['GET'])
@token_required
def get_room_info_search(current_user):
    try:
        searchName = request.args.get('searchName')
        check = re.search('[!#$%^&*()='',.?":{}|<>]', str(searchName))
        if check is None:
            searchResults = Exam_Room.searchRoomRecord(searchName)
            return jsonify({'status': 'success',
                            'search_results': searchResults,
                            }), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400
