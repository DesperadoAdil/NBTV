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


#List
@app.route('/api/list', methods = ['GET'])
def list():
    ret = []
    Classlist = Classrooms.query.filter_by(visible = "yes").all()
    for Class in Classlist:
        if Class is None:
            print ("No living room!")
            break
        else:
            dic = {}
            dic["id"] = str(Class.id)
            dic["teacher"] = Class.teacher
            dic["title"] = Class.title
            dic["thumbnail"] = Class.thumbnail
            dic["password"] = Class.password
            dic["url"] = Class.url
            dic["studentlist"] = Class.studentlist
            dic["teacherlist"] = Class.teacherlist
            dic["audiencelist"] = Class.audiencelist
            dic["visible"] = Class.visible
            ret.append(dic)
    print (json.dumps(ret))
    return json.dumps(ret)
