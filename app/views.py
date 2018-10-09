from flask import *
from app import app
from sqlalchemy import and_, or_, not_

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/api/user/login', methods = ['POST'])
def login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    job = request.form.get('job', None)
    print (str(username) + '\n' + str(password))
    
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
    

@app.route('/user/register', methods = ['POST'])
def register():
    phonenumber = request.form.get('mobile', None)
    if not phonenumber:
        return '{ status : "error" }'
    
    '''
        TextMessage Verification
    '''
    
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    job = request.form.get('job', None)
    verification = request.form.get('verification', None)

    if not username or not password or not job or not verification:
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
