# -*- coding: UTF-8 -*-
from flask import *
from . import classlist
from ..models import *
from ..classroom.Classroom import classroomManager
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
            dic = classroomManager.dict(Class)
            ret.append(dic)
    print (json.dumps(ret))
    return json.dumps(ret)
