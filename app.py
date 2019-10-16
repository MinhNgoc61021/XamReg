import logging

from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL  # cmd install flask-mysql
from flask_cors import CORS
app = Flask(__name__)

Debug = True

mysql = MySQL()
# create app
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'newroot'
app.config['MYSQL_DATABASE_PASSWORD'] = '528491'
app.config['MYSQL_DATABASE_DB'] = 'Demologin'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# enable CORS
CORS(app)

# get log
logging.getLogger('flask_cors').level = logging.DEBUG


@app.route('/register-form')
def register_form():
    return jsonify('Hello World')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    print(username + " " + password)

    cursor.execute('select * from user where Username = "' + username + '" and Password ="' + password + '"')
    user_tuple = cursor.fetchone()
    if user_tuple is None:
        return 'Account not exist'
    else:
        return 'Logged-in'

@app.route('/create-account', methods=['POST'])
def create_account():
    username = request.form['new-username-input']
    email = request.form['new-email-input']
    fullname = request.form['new-fullname-input']
    password = request.form['new-password-input']
    confirm_password = request.form['confirm-password-input']
    cursor = mysql.connect().cursor()
    cursor.execute('select * from user where Username = "' + username + '"')
    is_user_exist = cursor.fetchone()
    if is_user_exist is None:
        cursor.execute('insert into user(password, username, fullname, email) values ("' + password + '", "' + username + '", "' + fullname + '", "' + email + '")')
    else:
        return 'LOL'


if __name__ == '__main__':
    app.run(debug=True)
