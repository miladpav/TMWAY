from flask import Blueprint, request, render_template, redirect, url_for
from .forms import Form

from .profile import profile_route

auth = Blueprint('auth', __name__)

auth.register_blueprint(profile_route)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return 'success_login'


@auth.route('/signup', methods=['GET', 'POST'])
def Signup():
    signup_form = Form()
    if request.method == 'GET':
        return render_template('signup.html', form=signup_form)
    
    elif request.method == 'POST':
        if signup_form.validate_on_submit():
            print(signup_form.username.data)
            return redirect(url_for('profile_route.Profile', firstName=signup_form.firstName.data, lastName=signup_form.lastName.data))
        else:
            return 'data invalid'

        


@auth.route('/logout')
def logout():
    return 'logout'
