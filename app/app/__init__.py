from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
socketio = SocketIO(app)

from .user import user as user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/api/user')

from .developer import developer as developer_blueprint
app.register_blueprint(developer_blueprint, url_prefix='/developer')

from .classlist import classlist as classlist_blueprint
app.register_blueprint(classlist_blueprint, url_prefix='/api/list')

from .resource import resource as resource_blueprint
app.register_blueprint(resource_blueprint, url_prefix = '/api/resource')

from .classroom import classroom as classroom_blueprint
app.register_blueprint(classroom_blueprint, url_prefix = '/api/classroom')

from .classroom_stu import classroom_stu as classroom_stu_blueprint
app.register_blueprint(classroom_stu_blueprint, url_prefix = '/api/classroom_stu')

from app import views, models
