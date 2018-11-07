from flask import Blueprint

socketserver = Blueprint('socketserver', __name__)

from . import server
