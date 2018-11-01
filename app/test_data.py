from app import db
from app.models import *
import json

classroom = Classrooms()
classroom.vid = 242544
classroom.teacher = "adil"
classroom.title = "Test"
classroom.thumbnail = "/static/image/test.jpg"
classroom.password = "123456"
classroom.url = "242544"
classroom.rtmpUrl = ""
classroom.studentlist = json.dumps(["stu1", "stu2"])
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
