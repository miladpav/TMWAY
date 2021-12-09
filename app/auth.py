from flask import Blueprint, request, render_template, redirect, url_for

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
    if request.method == 'GET':
        return render_template('signup.html')
    
    elif request.method == 'POST':
        firstName = request.form['firtName']
        lastName = request.form['lastName']
        context = {'FirstName': firstName, 'LastName': lastName}
        return redirect(url_for('profile_route.Profile', firstName=firstName, lastName=lastName))
        


@auth.route('/logout')
def logout():
    return 'logout'
