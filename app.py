import logging

from flask import Flask, request, render_template, jsonify
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL
from flask_cors import CORS
app = Flask(__name__)
bcrypt = Bcrypt(app)

Debug = True

mysql = MySQL()
# create app
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'newroot'
app.config['MYSQL_DATABASE_PASSWORD'] = '528491'
app.config['MYSQL_DATABASE_DB'] = 'xamreg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# enable CORS
CORS(app)

# get log
logging.getLogger('flask_cors').level = logging.DEBUG


@app.route('/register-form')
def register_form():
    return jsonify('Hello There')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    user_form = request.get_json()
    cursor = mysql.connect().cursor()
    print(user_form)
    username = user_form.get('Username')
    password = user_form.get('Password')
    cursor.execute('select * from user where Username = "' + username + '" and Password ="' + password + '"')
    user_tuple = cursor.fetchone()
    if user_tuple is None:
        return jsonify("Fuck")
    else:
        return jsonify("Proceed")

if __name__ == '__main__':
    app.run(debug=True)
