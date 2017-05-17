# homepage and dashboard frontend

from flask import render_template
from flask_login import current_user, login_required

from . import home


@home.route('/')
def homepage():
    """
    render homepage template on '/' route.
    """
    return render_template('home/index.html', title='Welcome')


# admin dashboard view
@home.route('/dashboard')
@login_required
def dashboard():
    """
    render dashbaord template on '/dashboard' route
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('home/dashboard.html', title='Dashboard')