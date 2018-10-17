# -*- coding: UTF-8 -*-
from flask import *
from . import classlist
from ..models import *
import json

#List
@classlist.route('/', methods = ['GET'])
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
            dic["vid"] = str(Class.vid)
            dic["teacher"] = Class.teacher
            dic["title"] = Class.title
            dic["thumbnail"] = Class.thumbnail
            dic["password"] = Class.password
            dic["url"] = Class.url
            dic["studentlist"] = Class.studentlist
            dic["teacherlist"] = Class.teacherlist
            dic["audiencelist"] = Class.audiencelist
            dic["visible"] = Class.visible
            dic["createtime"] = str(Class.createtime)
            ret.append(dic)
    print (json.dumps(ret))
    return json.dumps(ret)
