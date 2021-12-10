from .views.auth import auth
from .views.index import index_api
from .views.tmway import tmway_api
from .views.profile import profile_route
from flask import Flask
from config import db
## --------------------------------------------------------------------- ##


app = Flask(__name__)
app.config.from_object('config')

app.config['SECRET_KEY'] = 'my_password'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(index_api, url_prefix='/index')
app.register_blueprint(tmway_api)
app.register_blueprint(auth)
app.register_blueprint(profile_route)
    
