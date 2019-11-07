from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from api.entity_db import *

# write this in cmd
# for Windows
# set FLASK_ENV=run.py
# set FLASK_ENV=development
# flask run

# for Linux/Mac OS
# export FLASK_APP=run.py
# export FLASK_ENV=development
# flask run

app = Flask(__name__)
CORS(app)
api = Api(app)
hashing = Bcrypt(app)


@app.route('/init_admin')
def init_admin():
    password_hash = hashing.generate_password_hash('12345')
    check_user = User.isExist('MinhNgoc')
    # check_user_role = User_Role.isExist(check_user.UserID)
    if check_user:
        return "Admin has already been created"
    else:
        add_admin = User.create('MinhNgoc', password_hash, 'Nguyen Ngoc Minh', '1999-12-18',
                                'Needforspeed1900@gmail.com', 'Male', 'none')
        User_Role.create(add_admin.UserID, 'Admin')
        return 'Hello There ' + add_admin.Fullname


if __name__ == "__main__":
    app.run(port=5000, debug=True)
