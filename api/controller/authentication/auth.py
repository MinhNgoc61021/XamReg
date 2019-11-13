from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    g,
    request,
    session,
    jsonify
)
from flask_cors import CORS
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
            session[username] = 'active'
            print(session)
            return jsonify("Proceed")
