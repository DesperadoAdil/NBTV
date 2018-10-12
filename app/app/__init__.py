from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .user import user as user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/api/user')

from app import views, models
