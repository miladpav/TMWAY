from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .profile import profile_route
from .tmway import tmway_api
from .index import index_api
from .auth import auth


## --------------------------------------------------------------------- ##

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(index_api)
app.register_blueprint(tmway_api)
app.register_blueprint(auth)
app.register_blueprint(profile_route)


