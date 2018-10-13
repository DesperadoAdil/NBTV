from flask import Blueprint

classlist = Blueprint('classlist', __name__)

from . import views
