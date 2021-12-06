from flask import render_template, Blueprint


profile_route = Blueprint('profile_route', __name__)


@profile_route.route('/profile')
def Profile():
    return render_template('profile.html')