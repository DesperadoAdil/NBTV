# -*- coding: UTF-8 -*-
from flask import *
from app import app
from sqlalchemy import and_, or_, not_
from app.textMessage import TextMessage
from .models import *
import json, os
import random

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


#Display_pdf
@app.route('/display', methods = ['GET', 'POST'])
def dispolay():
    '''path = "pdf/" + path
    parent_path = os.path.dirname(__file__)
    parent_path = os.path.dirname(parent_path)
    parent_path = os.path.dirname(parent_path)
    parent_path = os.path.join(parent_path, path)
    print (parent_path)
    
    resp = make_response(open(parent_path, encoding = 'UTF-8').read())
    resp.headers["Content-type"]="application/json;charset=UTF-8"
    return resp'''
    return render_template("displaypdf.html")


#Show_pdf
@app.route('/showpdf/<filename>', methods = ['GET', 'POST'])
def show_pdf(filename):
    path = os.path.dirname(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    os.chdir(path)
    os.chdir("pdfjs")
    os.chdir("web")
    path = os.getcwd()
    print (path)
    resp = make_response(open(os.path.join(path, "viewer.html")).read())
    resp.headers["Content-type"]="application/json;charset=UTF-8"
    return resp
    
