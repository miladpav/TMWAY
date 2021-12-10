from flask import Blueprint, request, render_template, redirect, url_for, make_response, jsonify
from flask import current_app as app
from ..models import UserModel
from config import db
from ..forms import Form
from .profile import profile_route


auth = Blueprint('auth', __name__)
auth.register_blueprint(profile_route)


@auth.route('/login', methods=['GET', 'POST'])
def Login(username):
    if request.method == 'GET':
        return render_template('login.html', username=username)
    elif request.method == 'POST':
        return 'success_login'


@auth.route('/signup', methods=['GET', 'POST'])
def Signup():
    signup_form = Form()
    if request.method == 'GET':
        return render_template('signup.html', form=signup_form)
    
    elif request.method == 'POST':
        if signup_form.validate_on_submit():
            username = signup_form.username.data
            password = signup_form.password.data
            firstName = signup_form.firstName.data
            lastName = signup_form.lastName.data
            newUser = UserModel(username=username, password=password, firstName=firstName, lastName=lastName )
            print("------------------------------------")
            print("new User id = ", newUser)
            print("------------------------------------")
            db.session.add(newUser)
            db.session.commit()
            print(signup_form.username.data)
            user = UserModel.query.filter_by(username=username).first()
            print(user.id, " = ", user.username)
            user_id = user.id
            return redirect(url_for('profile_route.Profile', user_id=user_id))
        else:
            return make_response(jsonify({'message': f'could not create user', 'status': 'Error'}), 400)

        


@auth.route('/logout')
def logout():
    return 'logout'
