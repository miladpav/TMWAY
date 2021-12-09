from flask import render_template, Blueprint

profile_route = Blueprint('profile_route', __name__)

@profile_route.route('/profile/<string:firstName>-<string:lastName>')
def Profile(firstName, lastName):
    context = {'firstName': firstName, 'lastName': lastName}
    print(f"firstName: {firstName} lastName: {lastName}")
    return render_template('profile.html', context=context)