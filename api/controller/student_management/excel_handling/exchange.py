from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    g,
    request,
    session,
    jsonify,
    logging
)

from openpyxl import load_workbook
excel_handling = Blueprint('import_export', __name__, url_prefix='/handling')


# to get excel data
@excel_handling.route('/upload', methods=['POST'])
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
    for i in range(1, max_row + 1):

        # iterate over all columns
        for j in range(1, max_column + 1):
            # get particular cell value
            cell_obj = sheet.cell(row=i, column=j)
            # print cell value
            print(cell_obj.value, flush=True, end=' | ')
        # print new line
        print('\n')
    return jsonify('coool')

