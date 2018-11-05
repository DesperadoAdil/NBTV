# -*- coding: UTF-8 -*-
from flask import *
import json
from . import classroom_stu
from ..models import Classrooms
from ..classroom.Classroom import classroomManager

#Url -> vid
@classroom_stu.route('/urlgetvid', methods = ['POST'])
def urlgetvid():
    ret = {}

    data = request.get_data()
    print (data)
    data = json.loads(data)

    url = data['url']

    classroom = classroomManager.search(url)
    if classroom is None:
        print ("Urlgetvid Error: No Such Classroom")
        ret["vid"] = ""
    else:
        ret["vid"] = str(classroom.vid);

    print (json.dumps(ret))
    return json.dumps(ret)
