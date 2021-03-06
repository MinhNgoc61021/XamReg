import re
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    current_app,
    jsonify
)
from flask_cors import CORS

from controller.time_conversion.asia_timezone import set_custom_log_time
from db.entity_db import User, Log

authentication = Blueprint('auth', __name__, url_prefix='/auth')
# create a blueprint is like creating a package
# ie: Sign In for authentication
CORS(authentication)


# Explain token_required function
# Ensure it contains the "Authorization" header with a string that looks like a JWT token
# Validate that the JWT is not expired, which PyJWT takes care of by throwing a ExpiredSignatureError if it is no longer valid
# Validate that the JWT is a valid token, which PyJWT also takes care of by throwing a InvalidTokenError if it is not valid
# If all is valid then the associated user is queried from the database and returned to the function the decorator is wrapping
def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Authentication is required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            check_user_jwt = User.getUser(data['sub'])
            if check_user_jwt is None:
                raise RuntimeError('User not found')
            print(check_user_jwt, flush=True)
            return f(check_user_jwt, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e, flush=True)
            return jsonify(invalid_msg), 401

    return _verify


@authentication.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        user_form = request.get_json()
        username = user_form.get('username')
        check_username = re.search('[!#$%^&*()='',?";:{}|<>]', username)
        password = user_form.get('password')
        check_password = re.search('[!#$%^&*()='',?";:{}|<>]', username)
        if (check_username is None) and (check_password is None):
            check_user = User.check_register(username, password)
            if check_user == 'Not found':
                return jsonify({'status': 'fail'})
            else:
                Log.create(str(check_user[0]['ID']), 'Đăng nhập vào hệ thống.', set_custom_log_time())

                token = jwt.encode({
                    'sub': username,  # representing username
                    'iat': datetime.utcnow(),  # issued at timestamp in seconds
                    'exp': datetime.utcnow() + timedelta(minutes=120)},
                    # the time in which the token will expire as seconds
                    current_app.config['SECRET_KEY'])
                return jsonify({'status': 'success',
                                'type': check_user[1],
                                'message': 'login successful',
                                'token': token.decode('UTF-8')})
        else:
            return jsonify({'status': 'Unauthorized'}), 401


@authentication.route('/get-user', methods=['GET'])
@token_required
def get_user(current_user):
    return jsonify({'status': 'success', 'ID': current_user['ID'],
                    'Fullname': current_user['Fullname'],
                    }), 200


@authentication.route('/update-password', methods=['PUT'])
@token_required
def update_password(current_user):
    currentUserID = request.get_json().get('UserID')
    newPassword = request.get_json().get('newPassword')
    confirmPassword = request.get_json().get('confirmPassword')

    if str(newPassword) == str(confirmPassword) and len(str(newPassword)) >= 5:
        User.updatePassword(currentUserID, str(newPassword))
        Log.create(str(current_user['ID']), 'Thay đổi mật khẩu', set_custom_log_time())
        return jsonify({'status': 'success'}), 200

    elif str(newPassword) != str(confirmPassword) or len(str(newPassword)) < 5:
        return jsonify({'status': 'password-not-meet-requirement'}), 202
    Log.create(str(current_user['ID']), 'Thay đổi mật khẩu', set_custom_log_time())
