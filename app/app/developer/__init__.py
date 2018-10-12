from flask import Blueprint

developer = Blueprint('developer', __name__, template_folder='templates')

from . import views
