from flask import *
from . import developer

@developer.route('/')
def hello():
    return render_template("developer.html")
