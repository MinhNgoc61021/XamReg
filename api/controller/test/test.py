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

tester = Blueprint('test', __name__, url_prefix='/test')

CORS(tester)


@tester.route('/hello_flask', mưthods=['GET'])
def test():
    return jsonify('Hello, Flask')


@tester.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
