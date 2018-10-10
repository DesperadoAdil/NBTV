from flask import *
from app import app
from sqlalchemy import and_, or_, not_
from app.textMessage import TextMessage
from .models import *
import json
import random

lastTextMessage = 0

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


#Login
@app.route('/api/user/login', methods = ['POST'])
def login():
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return '{ status : "error" }'

    if 'username' not in data or 'password' not in data or 'job' not in data:
        return '{ status : "error" }'
    
    username = data['username']
    password = data['password']
    job = data['job']
    if not username or not password or not job:
        return '{ status : "error" }'

    if job == 'teacher':
        teacher = Teachers.query.filter(and_(Teachers.username == username, Teachers.password == password)).first()
        if not teacher:
            teacher = Teachers.query.filter(and_(Teachers.phonenumber == username, Teachers.password == password)).first()
        if not teacher:
            return '{ status : "error" }'
        print ('Teacher login, username = ' + teacher.username)
    elif job == 'student':
        student = Students.query.filter(and_(Students.username == username, Students.password == password)).first()
        if not student:
            student = Students.query.filter(and_(Students.phonenumber == username, Students.password == password)).first()
        if not student:
            return '{ status : "error" }'
        print ('Student login, username = ' + student.username)
    
    return '{ status : "success" }'
    

#Register
@app.route('/api/user/register', methods = ['POST'])
def register():
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return '{ status : "error" }'

    if 'username' not in data or 'password' not in data or 'job' not in data or 'verification' not in data:
        return '{ status : "error" }'
    
    phonenumber = data['mobile']
    username = data['username']
    password = data['password']
    job = data['job']
    verification = data['verification']
    if not phonenumber or not username or not password or not job or not verification:
        return '{ status : "error" }'

    if int(verification) != lastTextMessage:
        return '{ status : "error" }'

    if job == 'teacher':
        teacher = Teachers(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(teacher)
        db.session.commit()
    elif job == 'student':
        student = Students(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(student)
        db.session.commit()

    return '{ status : "success" }'


#Verification
@app.route('/api/user/request_verification', methods = ['GET', 'POST'])
def verification():
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        return '{ status : "error" }'

    if 'mobile' not in data:
        return '{ status : "error" }'

    phonenumber = data['mobile']
    if not phonenumber:
        return '{ status : "error" }'
    
    message = TextMessage()
    businessID = random.randint(100000,999999)
    lastTextMessage = random.randint(100000,999999)
    message.sendSMS(businessID, phonenumber, lastTextMessage)
