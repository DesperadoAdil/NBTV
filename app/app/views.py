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


#Login
@app.route('/api/user/login', methods = ['POST'])
def login():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return json.dumps(ret)

    if 'username' not in data or 'password' not in data or 'job' not in data:
        return json.dumps(ret)
    username = data['username']
    password = data['password']
    job = data['job']
    if not username or not password or not job:
        return json.dumps(ret)
    if username=="" or password=="":
        return json.dumps(ret)

    if job == 'teacher':
        teacher = Teachers.query.filter(and_(Teachers.username == username, Teachers.password == password)).first()
        if not teacher:
            teacher = Teachers.query.filter(and_(Teachers.phonenumber == username, Teachers.password == password)).first()
        if not teacher:
            return json.dumps(ret)
        print ('Teacher login, username = ' + teacher.username)
        ret['username'] = teacher.username
        ret['password'] = teacher.password
        ret['rpassword'] = teacher.password
        ret['mobile'] = teacher.phonenumber
        ret['verification'] = ""
        ret['job'] = "teacher"
    elif job == 'student':
        student = Students.query.filter(and_(Students.username == username, Students.password == password)).first()
        if not student:
            student = Students.query.filter(and_(Students.phonenumber == username, Students.password == password)).first()
        if not student:
            return json.dumps(ret)
        print ('Student login, username = ' + student.username)
        ret['username'] = student.username
        ret['password'] = student.password
        ret['rpassword'] = student.password
        ret['mobile'] = student.phonenumber
        ret['verification'] = ""
        ret['job'] = "student"
    else:
        return json.dumps(ret)
        

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)
    

#Register
@app.route('/api/user/register', methods = ['POST'])
def register():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return json.dumps(ret)

    if 'username' not in data or 'password' not in data or 'rpassword' not in data or 'job' not in data or 'verification' not in data or 'mobile' not in data:
        return json.dumps(ret)
    phonenumber = data['mobile']
    username = data['username']
    password = data['password']
    rpassword = data['rpassword']
    job = data['job']
    verification = data['verification']
    if not phonenumber or not username or not password or not rpassword or not job or not verification:
        return json.dumps(ret)
    if phonenumber=="" or username=="" or password=="" or rpassword=="" or job=="" or verification=="":
        return json.dumps(ret)
    if password != rpassword:
        return json.dumps(ret)

    mess = Messages.query.filter(Messages.phonenumber == phonenumber).first()
    if mess is None:
        return json.dumps(ret)
    if verification != mess.message:
        print ('not equal:' + verification + ' !=  ' + mess.message)
        return json.dumps(ret)
    else:
        print ('equal!')
        mess.message = ''
        db.session.add(mess)
        db.session.commit()

    if job == 'teacher':
        teacher = Teachers.query.filter(Teachers.phonenumber == phonenumber).first()
        if teacher is not None:
            return json.dumps(ret)
        teacher = Teachers(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(teacher)
        db.session.commit()
    elif job == 'student':
        student = Students.query.filter(Students.phonenumber == phonenumber).first()
        if student is not None:
            return json.dumps(ret)
        student = Students(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(student)
        db.session.commit()
    else:
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#Verification
@app.route('/api/user/request_verification', methods = ['POST'])
def verification():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return json.dumps(ret)

    if 'mobile' not in data:
        return json.dumps(ret)
    phonenumber = data['mobile']
    if not phonenumber:
        return json.dumps(ret)
    if phonenumber=="" or len(phonenumber) < 11:
        return json.dumps(ret)

    message = TextMessage.TextMessage()
    businessID = str(random.randint(100000,999999))
    lastTextMessage = str(random.randint(100000,999999))
    print (businessID + '  ' + phonenumber + '  ' + lastTextMessage)
    dic = {}
    dic['code'] = lastTextMessage
    text = message.sendSMS(businessID, phonenumber, dic)
    print (text)

    mess = Messages.query.filter(Messages.phonenumber == phonenumber).first()
    if mess is None:
        mess = Messages(phonenumber=phonenumber, message=lastTextMessage)
    else:
        mess.message = lastTextMessage
    db.session.add(mess)
    db.session.commit()

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#List
@app.route('/api/list', methods = ['GET'])
def list():
    ret = []
    classlist = Classrooms.query.filter_by(visible = "yes").all()
    for Class in classlist:
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


#Change_password
@app.route('/api/user/change_password', methods = ['POST'])
def change_password():
    ret = {}
    ret["status"] = 'error'

    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return json.dumps(ret)

    if 'status' not in data or 'mobile' not in data or 'old_password' not in data or 'new_password' not in data or 'job' not in data:
        return json.dumps(ret)
    status = data['status']
    phonenumber = data['mobile']
    old_password = data['old_password']
    new_password = data['new_password']
    job = data['job']
    if not status or not phonenumber or not old_password or not new_password or not job:
        return json.dumps(ret)
    if status=="" or phonenumber=="" or old_password=="" or new_password=="":
        return json.dumps(ret)
    if old_password == new_password:
        return json.dumps(ret)

    if job == 'teacher':
        teacher = Teachers.query.filter_by(phonenumber = phonenumber).first()
        if teacher is None:
            return json.dumps(ret)
        if old_password != teacher.password:
            return json.dumps(ret)
        else:
            teacher.password = new_password
            db.session.add(teacher)
            db.session.commit()
    elif job == 'student':
        student = Students.query.filter_by(phonenumber = phonenumber).first()
        if student is None:
            return json.dumps(ret)
        if old_password != student.password:
            return json.dumps(ret)
        else:
            student.password = new_password
            db.session.add(student)
            db.session.commit()
    else:
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)
