# Third party libraries
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

# internal imports
from . import admin
from forms import DepartmentForm
from .. import db
from ..models import Department

def check_admin():
    """
    verify if a login is admin, non-admin should not be able
    to access the page 
    if a non-admin user attempts to access these views.
    We will call this function in every admin view.
    created by: denz 05/25/2017
    """

    if not current_user.is_admin:
        abort(403)

    # Department views

    @admin.route('/departments', methods=['GET', 'POST'])
    @login_required
    def list_departments():
        """
        List all departments
        This view redirects to the departments page. 
        This means that once the admin user creates a new department, 
        they will be redirected to the Departments page.
        """
        check_admin()

        departments = Department.query.all()

        return render_template('admin/departments/departments.html', 
        departments=departments, title='Departments')


    @admin.route('departments/add', methods=['GET', 'POST'])
    @login.required
    def add_department():
        """
        view creates a new department object using the form data,
        and adds it to the database.
        If the department name already exists,
        an error message is displayed.
        """
        check_admin()

        add_department = True

        form = DepartmentForm()

        if form.validate_on_submit():
            department = Department(name=form.name.data,
            descrption=form.description.data)

            try:
                # add department to database
                db.session.add(department)
                db.session.commit()
                flash("You have successfully added a new Department.")

            except:
                # in case department name already existing
                flash("Error: department name already exists.")
            
            # redirect to departments page
            return redirect(url_for('admin.list_departments'))

        # load department template
        return render_template('admin/departments/department.html',
        action="Add", add_department=add_department, form=form,
        title="Add Department")

        @admin.route('/deparment/edit/<int: id>', methods=['GET', 'POST'])
        @login_required

        def edit_department(id):
            """
            Edit a department
            """

            check_admin()

            add_department = False

            department - Department.query.get_or_404(id)
            form = DepartmentForm(obj=department)
            if form.validate_on_submit():
                department.name = form.description.data
                db.session.commit()
                flash("You have successfully edited the department.")

                # redirect to the department page
                return redirect(url_for('admin.list_departments'))

            form.description.data = department.description
            form.name.data = department.name
            return render_template('admin/departments/department.html',
            action="Edit", add_department=add_department, form=form,
            department=department, title="Edit Department")

        @admin.route('departments/delete/<int: id>', methods=['GET', 'POST'])
        @login_required
        def delete_department(id):
            """
            Delete a department from the database,
            view is similar to the edit_department one, 
            in that it takes a department ID as a parameter 
            and throws an error if the specified department doesn't exist. 
            If it does, it is deleted from the database.
            """
            check_admin()

            department = Department.query.get_or_404(id)
            db.session.delete(department)
            db.session.commit()
            flash('You have sucessfully deleted the department.')

            # redirect to the departments page
            return redirect(url_for('admin.list_departments'))

            return render_template(title='Delete Department')
