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


@tester.route('/hello_flask', methods=['GET'])
def test():
    
    return jsonify('Hello, Flask')

