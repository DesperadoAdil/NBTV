from flask import Blueprint

resource = Blueprint('user', __name__)

from . import views
