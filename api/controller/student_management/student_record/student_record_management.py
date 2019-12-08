from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.authentication.auth import token_required
from db.entity_db import User, Subject, Student_Status, Log
import datetime
import re

student_record_management = Blueprint('student_record_management', __name__, url_prefix='/record')


@student_record_management.route('/student-records', methods=['GET'])
@token_required
def get_student_info_record(current_user):
    try:
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')
        # print(sort_order, flush=True)
        # print(sort_field, flush=True)
        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        record = User.getRecord(page_index, per_page, sort_field, sort_order)

        return jsonify({'status': 'success',
                        'records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@student_record_management.route('/create-student-record', methods=['POST'])
@token_required
def create_new_studnet(current_user):
    try:
        newStudentID = request.get_json().get('newStudentID')
        newFullname = request.get_json().get('newFullname')
        newCourseID = request.get_json().get('newCourseID')
        newDob = request.get_json().get('newDob')
        newGender = request.get_json().get('newGender')
        print(newStudentID, flush=True)
        print(newFullname, flush=True)
        print(newCourseID, flush=True)
        print(newDob, flush=True)
        print(newGender, flush=True)
        # check validation
        checkStudentID = re.search('^\d{8}$', str(newStudentID).replace(' ', ''))
        checkFullname = re.search('^[a-zA-Z]+', str(newFullname))
        checkDob = re.search('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',
                             str(newDob))
        checkGender = re.search('(Nam|Nữ)', str(newGender))
        checkCourseID = re.search('^[K|k][1-9][0-9][A-Za-z]+[1-9]*', str(newCourseID))
        Log.create(current_user['ID'],
                   'Tạo thêm sinh viên có MSSV: ' + newStudentID + ' vào hệ thống.',
                   datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        if (checkStudentID is not None) and (checkFullname is not None) and (
                checkDob is not None) and (
                checkGender is not None) and (checkCourseID is not None):
            print('OK1', flush=True)


            newStudent = User.create(newStudentID, newStudentID + '@vnu.edu.vn', newStudentID, newFullname, newDob, newGender, newCourseID, 'Student')
            print('OK2', flush=True)
            if newStudent is False:
                return jsonify({'status': 'bad-request'}), 400
            else:
                return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400

@student_record_management.route('/search-student-record', methods=['GET'])
@token_required
def get_student_info_search(current_user):
    try:
        searchID = request.args.get('searchID')
        check = re.search('[!#$%^&*()='',.?":{}|<>]', str(searchID))
        if check is None:
            searchResults = User.searchStudentRecord(searchID)
            return jsonify({'status': 'success',
                            'search_results': searchResults,
                            }), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400


@student_record_management.route('/student-status-records', methods=['GET'])
@token_required
def get_subject_status_record(current_user):
    try:
        studentID = request.args.get('StudentID')
        status_type = request.args.get('type')
        page_index = request.args.get('page_index')
        per_page = request.args.get('per_page')
        sort_order = request.args.get('sort_order')
        sort_field = request.args.get('sort_field')

        print(studentID, flush=True)
        print(status_type, flush=True)
        print(page_index, flush=True)
        print(per_page, flush=True)
        print(sort_order, flush=True)
        print(sort_field, flush=True)

        # FYI: User.getRecord function return a tuple, [0] is the records data, and [1] is the pagination data
        record = Subject.getRecord(studentID, status_type, page_index, per_page, sort_field, sort_order)
        print(record[1], flush=True)
        print(record[0], flush=True)
        return jsonify({'status': 'success',
                        'records': record[0],
                        'page_number': record[1].page_number,
                        'page_size': record[1].page_size,
                        'num_pages': record[1].num_pages,
                        'total_results': record[1].total_results,
                        }), 200

    except:
        return jsonify({'status': 'bad-request'}), 400


@student_record_management.route('/remove-student-record', methods=['DELETE'])
@token_required
def remove_student_info_record(current_user):
    try:
        # print(request.get_json('studentID'), flush=True)
        record = request.get_json()
        studentID = record.get('delStudentID')
        User.delRecord(str(studentID))
        Log.create(current_user['ID'],
                   'Xóa thông tin của sinh viên có MSSV: ' + studentID + ' khỏi hệ thống.',
                   datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@student_record_management.route('/remove-student-status-record', methods=['DELETE'])
@token_required
def remove_subject_record(current_user):
    try:
        # print(request.get_json('studentID'), flush=True)
        record = request.get_json()
        studentID = record.get('delStudentID')
        subjectID = record.get('delSubjectID')
        Student_Status.delRecord(str(studentID), str(subjectID))
        Log.create(current_user['ID'],
                   'Xóa mã môn ' + subjectID + ' của sinh viên có MSSV: ' + studentID + ' khỏi hệ thống.',
                   datetime.datetime.now())

        return jsonify({'status': 'success'}), 200
    except:
        return jsonify({'status': 'bad-request'}), 400


@student_record_management.route('/update-student-record', methods=['PUT'])
@token_required
def update_student_info_record(current_user):
    try:
        new_update = request.get_json()
        currentStudentID = new_update.get('currentStudentID')
        newStudentID = new_update.get('StudentID')
        newUsername = new_update.get('Username')
        newFullname = new_update.get('Fullname')
        newCourseID = new_update.get('CourseID')
        newDob = new_update.get('Dob')
        newGender = new_update.get('Gender')

        # print(currentStudentID, flush=True)
        # print(newStudentID, flush=True)
        # print(newUsername, flush=True)
        # print(newFullname, flush=True)
        # print(newPassword, flush=True)
        # print(newCourseID, flush=True)
        # print(newDob, flush=True)
        # print(newGender, flush=True)

        # check validation
        checkID = re.search('^\d{8}$', str(newStudentID).replace(' ', ''))
        checkUsername = re.search('^\d{8}@vnu.edu.vn$', str(newUsername))
        checkFullname = re.search('^[a-zA-Z]+', str(newFullname))
        checkDob = re.search('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',
                             str(newDob))
        checkGender = re.search('(Nam|Nữ)', str(newGender))
        checkCourseID = re.search('^[K|k][1-9][0-9][A-Za-z]+[1-9]*', str(newCourseID))

        print(checkID, flush=True)
        print(checkUsername, flush=True)
        print(checkFullname, flush=True)
        print(checkGender, flush=True)
        print(checkDob, flush=True)
        print(checkCourseID, flush=True)

        if (checkID is not None) and (checkUsername is not None) and (checkFullname is not None) and (
                checkDob is not None) and (
                checkGender is not None) and (checkCourseID is not None) and (
                newStudentID == newUsername.split('@')[0]):
            #  print('OK1', flush=True)
            User.updateRecord(currentStudentID, newStudentID, newUsername, newFullname, newCourseID, newDob, newGender)
            Log.create(current_user['ID'],
                       'Cập nhật thông tin của sinh viên vào hệ thống.',
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'bad-request'}), 400
    except:
        return jsonify({'status': 'bad-request'}), 400
