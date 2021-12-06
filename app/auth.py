from flask import Blueprint, request, render_template



auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def Signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return 'logout'
