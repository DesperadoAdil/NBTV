from flask import *
from app import app
from sqlalchemy import and_, or_, not_
from app.textMessage import TextMessage
from .models import *
import json
import random

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


#Display_pdf
@app.route('/display')
def dispolay():
    return render_template("displaypdf.html")
