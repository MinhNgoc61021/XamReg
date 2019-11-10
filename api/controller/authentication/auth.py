from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    g,
    request,
    session,
    jsonify
)
from flask_cors import CORS, cross_origin
from entity_db import User
authentication = Blueprint('auth', __name__, url_prefix='/auth')

# create a blueprint is like creating a package
# ie: Sign In for authentication
CORS(authentication)

@authentication.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return "Feminist"
    elif request.method == 'POST':
        user_form = request.get_json()
        print(user_form)
        username = user_form.get('Username')
        password = user_form.get('Password')
        check_user = User.check_register(username, password)

        if check_user is False:
            return jsonify("Flop")
        else:
            return jsonify("Proceed")

@authentication.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
