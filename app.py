from flask import Flask, request, render_template
from flaskext.mysql import MySQL  # cmd install flask-mysql

app = Flask(__name__)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'newroot'
app.config['MYSQL_DATABASE_PASSWORD'] = '528491'
app.config['MYSQL_DATABASE_DB'] = 'Demologin'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/register-form')
def register_form():
    return render_template('register-form.html')


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


if __name__ == '__main__':
    app.run(debug=True)
