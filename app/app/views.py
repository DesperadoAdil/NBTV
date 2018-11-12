# -*- coding: UTF-8 -*-
from flask import *
from app import app
from sqlalchemy import and_, or_, not_
from app.textMessage import TextMessage
from .models import *
import json, os
import random

#Display_pdf
@app.route('/display', methods = ['GET', 'POST'])
def dispolay():
    return render_template("displaypdf.html")


#get pdf file
@app.route('/pdf/<path>')
def getPDF(path):
    return send_from_directory('/mnt/NBTV', path)

@app.route('/img_class/<path>')
def getImg(path):
	print('get image: ', path)
	image_data = open(os.path.join('/mnt/NBTV_Img', path), "rb").read()
    response = make_response(image_data)
    if path[-3:] == 'jpg' or path[-4:] == 'jpeg':
    	response.headers['Content-Type'] = 'image/jpeg'
    else:
    	response.headers['Content-Type'] = 'image/png'
    return response
	# return send_from_directory('/mnt/NBTV_Img', path, as_attachment=True)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")
