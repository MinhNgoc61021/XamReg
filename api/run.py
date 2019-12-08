from flask_cors import CORS
from flask_restful import Api
from db.entity_db import User
from controller import create_app

# write this in cmd
# for Windows
# set FLASK_ENV=run.py
# set FLASK_ENV=development
# flask run

# for Linux/Mac OS
# export FLASK_APP=run.py
# export FLASK_ENV=development
# flask run

app = create_app()
app.config['SECRET_KEY'] = 'IsBLK8lCfYOF7VHNflxkSg'
api = Api(app)
CORS(app)


# create new admin here, change the username, password
@app.route('/init_admin')
def init_admin():
    check_user = User.isExist('NamPham')
    # check_user_role = User_Role.isExist(check_user.UserID)
    if check_user:
        return 'OK, an admin has already been created.'
    else:
        # fullname = 'Nguyễn Ngọc Minh'
        # print(fullname, flush=True)
        add_admin = User.create('Admin69', 'MinhNgoc', '12345', 'Nguyễn Mĩnh Ngháo', '1999-12-18',
                                'Male', 'INTAdmin', 'Admin')


# @app.route('/hello')
# def hello():
#     return 'hello'


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
