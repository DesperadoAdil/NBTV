from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .user import user as user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/api/user')

from .developer import developer as developer_blueprint
app.register_blueprint(developer_blueprint, url_prefix='/developer')

from .classlist import classlist as classlist_blueprint
app.register_blueprint(classlist_blueprint, url_prefix='/api/list')

from .resource import resource as resource_blueprint
app.register_blueprint(resource_blueprint, url_prefix = '/api/resource')

from .classroom import classroom as classroom_blueprint
app.resource_blueprint(classroom_blueprint, url_prefix = '/api/classroom')

from app import views, models
