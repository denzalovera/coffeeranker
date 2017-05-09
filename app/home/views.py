# homepage and dashboard frontend

from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    render homepage template on '/' route.
    """
    return render_template('home/index.html', title='Welcome')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    render dashbaord template on '/dashboard' route
    """

    return render_template('/home/dashboard.html', title='Dashboard')