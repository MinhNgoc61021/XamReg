import functools

from flask import (
    Blueprint,
    # Blueprint is a way to organize a group of related views and other code
    # There will be 2 blueprints: one for authentication and one for posts function
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from backend.db.entity_db import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
