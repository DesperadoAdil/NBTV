# -*- coding: UTF-8 -*-
from app.test.BaseTestCase import BaseTestCase
from app import db
from app.models import *
import unittest
import json

class DataTest(BaseTestCase):
    def test_database(self):
        print ("Test:Database===============================")

        db.drop_all()
        db.create_all()

        classroom = Classrooms()
        classroom.vid = 242544
        classroom.teacher = "adil"
        classroom.title = "Test"
        classroom.thumbnail = "/static/image/test.jpg"
        classroom.password = "123456"
        classroom.url = "242544"
        classroom.rtmpUrl = ""
        classroom.mode = "protected"
        classroom.studentlist = json.dumps(["stu1", "stu2"])
        db.session.add(classroom)

        classroom = Classrooms()
        classroom.vid = 250810
        classroom.teacher = "adil"
        classroom.title = "小葵花妈妈课堂"
        classroom.thumbnail = "/static/image/123456.jpg"
        classroom.password = "123456"
        classroom.url = "123456"
        classroom.rtmpUrl = "rtmp://push2.videocc.net/recordfe/7181857ac220181030221452650"
        classroom.mode = "protected"
        db.session.add(classroom)

        teacher = Teachers()
        teacher.phonenumber = "17799163760"
        teacher.username = "adil"
        teacher.password = "123456"
        db.session.add(teacher)

        student1 = Students()
        student1.phonenumber = "17799163760"
        student1.username = "stu1"
        student1.password = "123456"
        student1.classroomlist = json.dumps(["242544"])
        db.session.add(student1)

        student2 = Students()
        student2.phonenumber = "17799163761"
        student2.username = "stu2"
        student2.password = "123456"
        student2.classroomlist = json.dumps(["242544"])
        db.session.add(student2)

        db.session.commit()
