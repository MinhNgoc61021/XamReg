import os
from flask import Flask
from flask_bcrypt import Bcrypt
from backend.model.entity_db import *


# before run do this
# cmd set FLASK_APP=controller
# cmd set FLASK_ENV=development

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    hashing = Bcrypt(app)
    from . import auth
    app.register_blueprint(auth.auth)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    return app
