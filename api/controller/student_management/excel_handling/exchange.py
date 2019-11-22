from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    jsonify
)
from controller.db.entity_db import User, Subject, Student_Status
from openpyxl import load_workbook
from controller.authentication.auth import token_required

excel_handling = Blueprint('import_export', __name__, url_prefix='/handling')


# to get excel data
@excel_handling.route('/upload', methods=['POST'])
@token_required
def upload(auth):
    print(request.files['student_list_excel'], flush=True)
    # load file
    excel_file = load_workbook(request.files['student_list_excel'])
    # select Danh sách sinh viên.xlsx
    sheet = excel_file.active

    # get max row count
    max_row = sheet.max_row
    # get max column count
    max_column = sheet.max_column

    # When the excel file are included with student, subject info & status
    if max_column == 8:
        # set excel_data to get data in order to create new account, subject, qualification for students to SQLAlchemy
        for i in range(2, max_row + 1):
            excel_data = {
                'ID': None,
                'fullname': None,
                'dob': None,
                'gender': None,
                'courseID': None,
                'subjectID': None,
                'subjectTitle': None,
                'status': None,
            }
            # Iterate over the dict and all the columns
            for j, index in zip(range(1, max_column + 1), excel_data):
                # add data to excel_data dict
                excel_data[index] = sheet.cell(row=i, column=j).value
            print(excel_data, flush=True)
            # add students to database
            init_student = User.create(str(excel_data['ID']),
                                       str(excel_data['ID']) + '@vnu.edu.vn',
                                       str(excel_data['ID']),
                                       excel_data['fullname'],
                                       excel_data['dob'],
                                       excel_data['gender'],
                                       excel_data['courseID'],
                                       'Student')
            # add subject to database
            init_subject = Subject.create(excel_data['subjectID'],
                                          excel_data['subjectTitle'])
            # add qualified and unqualified students to database
            init_qualified_student = Student_Status.create(excel_data['ID'],
                                                           excel_data['subjectID'], excel_data['status'])

            return jsonify({'status': 'success'}), 200

    # When the excel file are included of only student info
    elif max_column == 5:
        # set excel_data to get data in order to create new account only for students to SQLAlchemy
        for i in range(2, max_row + 1):
            excel_data = {
                'ID': None,
                'fullname': None,
                'dob': None,
                'gender': None,
                'courseID': None,
            }
            # Iterate over the dict and all the columns
            for j, index in zip(range(1, max_column + 1), excel_data):
                # add data to excel_data dict
                excel_data[index] = sheet.cell(row=i, column=j).value
                print(excel_data, flush=True)
                # add students to database
            init_student = User.create(str(excel_data['ID']),
                                       str(excel_data['ID']) + '@vnu.edu.vn',
                                       str(excel_data['ID']),
                                       excel_data['fullname'],
                                       excel_data['dob'],
                                       excel_data['gender'],
                                       excel_data['courseID'],
                                       'Student')

            return jsonify({'status': 'success'}), 200

    # When the excel file are included of only student info
    # This requires student account to have been existed before being added
    elif max_column == 4:
        for i in range(2, max_row + 1):
            excel_data = {
                'ID': None,
                'subjectID': None,
                'subjectTitle': None,
                'status': None,

            }
            # Iterate over the dict and all the columns
            for j, index in zip(range(1, max_column + 1), excel_data):
                # add data to excel_data dict
                excel_data[index] = sheet.cell(row=i, column=j).value
                print(excel_data, flush=True)
            # add subject to database
            init_subject = Subject.create(excel_data['subjectID'],
                                          excel_data['subjectTitle'])
            # add qualified and unqualified students to database
            init_qualified_student = Student_Status.create(excel_data['ID'],
                                                           excel_data['subjectID'], excel_data['status'])

            return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'}), 400
