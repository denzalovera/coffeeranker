# frontend routes for auth goes here.

# third-party imports
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# local imports
from . import auth
from forms import RegistrationForm, LoginForm
from .. import db
from ..models import Employee


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    handle request for register route.
    adds employee/user to database through registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add employee to DB
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle request to /login route
    login employee through login form
    """

    form = LoginForm()
    if form.validate_on_submit():

        # verify if user exist on DB
        # verify if password match password on DB

        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):

            # login user
            logout_user(employee)

            return redirect(url_for('home.dashboard'))

        else:
            flash('Invalid email or password')

    return render_template('auth/login.html', form=form, title='login')


@auth.route('/logout')
@login_required
def logout():
    """
    handle request to /logout route
    logout a user through logout link
    """

    logout_user()
    flash('You have successfully been logged out.')

    # redirect to login page
    return redirect(url_for('auth.login'))
