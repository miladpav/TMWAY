from flask import render_template, Blueprint
from config import db
from ..models import UserModel

profile_route = Blueprint('profile_route', __name__)

@profile_route.route('/profile/<int:user_id>')
def Profile(user_id):
    user = UserModel.query.filter_by(id=user_id).first()
    id = user.id
    username = user.username
    password = user.password
    firstName = user.firstName
    lastName = user.lastName
    context = {'firstName': firstName, 'lastName': lastName, 'id': id, 'username': username, 'password': password}
    return render_template('profile.html', context=context)