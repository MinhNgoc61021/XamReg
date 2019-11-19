from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    request,
    current_app,
    jsonify
)
from flask_cors import CORS
from controller.db.entity_db import User
import jwt
from datetime import datetime, timedelta
from functools import wraps

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
            'message': 'Expired token. Reauthentication is required.',
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
        password = user_form.get('password')
        check_user = User.check_register(username, password)
        if check_user is False:
            return jsonify({'status': 'fail'})
        else:
            token = jwt.encode({
                'sub': username,  # representing username
                'iat': datetime.utcnow(),  # issued at timestamp in seconds
                'exp': datetime.utcnow() + timedelta(minutes=30)},  # the time in which the token will expire as seconds
                current_app.config['SECRET_KEY'])
            return jsonify({'status': 'success',
                            'type': 'admin',
                            'message': 'login successful',
                            'token': token.decode('UTF-8')})


@authentication.route('/get-user', methods=['GET'])
@token_required
def get_user(current_user):
    # print(current_user['Username'], flush=True)
    return jsonify({'ID': current_user['ID'],
                    'Username': current_user['Username'],
                    'Fullname': current_user['Fullname'],
                    'Dob': current_user['Dob'],
                    'Gender': current_user['Gender']
                    })


