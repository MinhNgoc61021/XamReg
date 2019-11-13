from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from controller import create_app
from entity_db import *
from flask import session, g
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
hashing = Bcrypt(app)
CORS(app)


# create new admin here, change the username, password
@app.route('/init_admin')
def init_admin():
    password_hash = hashing.generate_password_hash('12345')
    check_user = User.isExist('MinhNgoc')
    # check_user_role = User_Role.isExist(check_user.UserID)
    if check_user:
        return 'OK, an admin has already been created.'
    else:
        add_admin = User.create('Admin1','MinhNgoc', password_hash, 'Nguyễn Ngọc Minh', '1999-12-18',
                                'Needforspeed1900@gmail.com', 'Male')
        User_Role.create(add_admin.UserID, 'Admin')


@app.route('/hello')
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
