from flask import Blueprint, request, render_template



auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return 'success_login'


@auth.route('/signup')
def Signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return 'logout'
