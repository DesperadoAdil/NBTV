from flask import Blueprint

classroom_stu = Blueprint('classroom_stu', __name__)

from . import views
