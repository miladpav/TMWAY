from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .profile import profile_route
from .tmway import tmway_api
from .index import index_api
from .auth import auth


## --------------------------------------------------------------------- ##

db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_password'
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

app.register_blueprint(index_api)
app.register_blueprint(tmway_api)
app.register_blueprint(auth)
app.register_blueprint(profile_route)


