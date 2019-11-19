from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request
)
from controller.db.entity_db import User, Subject, Student_Status
from openpyxl import load_workbook
from controller.authentication.auth import token_required

excel_handling = Blueprint('import_export', __name__, url_prefix='/handling')


# to get excel data
@excel_handling.route('/upload', methods=['POST'])
@token_required
def upload():
    print(request.files['student_list_excel'], flush=True)
    # load file
    excel_file = load_workbook(request.files['student_list_excel'])
    # select Danh sách sinh viên.xlsx
    sheet = excel_file.active

    # get max row count
    max_row = sheet.max_row
    # get max column count
    max_column = sheet.max_column

    # iterate over all cells
    # iterate over all rows
    for i in range(2, max_row + 1):
        # set excel_data to get data in order to create new User, Subject, Qualification for students to SQLAlchemy
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

        # add students to database
        init_student = User.create(excel_data['ID'],
                                   excel_data['ID'] + '@vnu.edu.vn',
                                   excel_data['ID'],
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
    return 'Success'
