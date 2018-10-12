from flask import *
from . import user
from sqlalchemy import and_, or_, not_
from ..textMessage import TextMessage
from ..models import *
import json
import random

#Login
@user.route('/login', methods = ['POST'])
def login():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        ret['status']='error:无表单！'
        return json.dumps(ret)

    if 'username' not in data or 'password' not in data or 'job' not in data:
        ret['status']='error:表单缺失！'
        return json.dumps(ret)
    username = data['username']
    password = data['password']
    job = data['job']
    if not username or not password or not job:
        ret['status']='error:用户名或密码缺失！'
        return json.dumps(ret)
    if username=="" or password=="":
        ret['status']='error:用户名或密码为空！'
        return json.dumps(ret)

    if job == 'teacher':
        teacher = Teachers.query.filter(and_(Teachers.username == username, Teachers.password == password)).first()
        if not teacher:
            teacher = Teachers.query.filter(and_(Teachers.phonenumber == username, Teachers.password == password)).first()
        if not teacher:
            ret['status']='error:用户名或密码错误！'
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
            ret['status']='error:用户名或密码错误！'
            return json.dumps(ret)
        print ('Student login, username = ' + student.username)
        ret['username'] = student.username
        ret['password'] = student.password
        ret['rpassword'] = student.password
        ret['mobile'] = student.phonenumber
        ret['verification'] = ""
        ret['job'] = "student"
    else:
        ret['status']='error:请选择学生或教师！'
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#Register
@user.route('/register', methods = ['POST'])
def register():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        ret['status']='error:无表单！'
        return json.dumps(ret)

    if 'username' not in data or 'password' not in data or 'rpassword' not in data or 'job' not in data or 'verification' not in data or 'mobile' not in data:
        ret['status']='error:表单缺失！'
        return json.dumps(ret)
    phonenumber = data['mobile']
    username = data['username']
    password = data['password']
    rpassword = data['rpassword']
    job = data['job']
    verification = data['verification']
    if not phonenumber or not username or not password or not rpassword or not job or not verification:
        ret['status']='error:注册信息缺失！'
        return json.dumps(ret)
    if phonenumber=="" or username=="" or password=="" or rpassword=="" or job=="" or verification=="":
        ret['status']='error:注册信息为空！'
        return json.dumps(ret)
    if password != rpassword:
        ret['status']='error:两次密码不一致！'
        return json.dumps(ret)

    mess = Messages.query.filter(Messages.phonenumber == phonenumber).first()
    if mess is None:
        ret['status']='error:请先发送短信验证码！'
        return json.dumps(ret)
    if verification != mess.message:
        print ('Not equal:' + verification + ' !=  ' + mess.message)
        ret['status']='error:验证码错误！'
        return json.dumps(ret)
    else:
        print ('Equal!')
    db.session.delete(mess)
    db.session.commit()

    if job == 'teacher':
        teacher = Teachers.query.filter(Teachers.phonenumber == phonenumber).first()
        if teacher is not None:
            ret['status']='error:用户已存在！'
            return json.dumps(ret)
        teacher = Teachers(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(teacher)
        db.session.commit()
    elif job == 'student':
        student = Students.query.filter(Students.phonenumber == phonenumber).first()
        if student is not None:
            ret['status']='error:用户已存在！'
            return json.dumps(ret)
        student = Students(phonenumber=phonenumber, username=username, password=password, classroomlist="")
        db.session.add(student)
        db.session.commit()
    else:
        ret['status']='error:请选择学生或教师！'
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#Verification
@user.route('/request_verification', methods = ['POST'])
def verification():
    ret = {}
    ret["status"] = 'error'
    
    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        ret['status']='error:无表单！'
        return json.dumps(ret)

    if 'mobile' not in data:
        ret['status']='error:表单缺失！'
        return json.dumps(ret)
    phonenumber = data['mobile']
    if not phonenumber:
        ret['status']='error:手机号缺失！'
        return json.dumps(ret)
    if phonenumber=="" or len(phonenumber) < 11:
        ret['status']='error:请输入正确的手机号！'
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


#Change_password
@user.route('/change_password', methods = ['POST'])
def change_password():
    ret = {}
    ret["status"] = 'error'

    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        ret['status']='error:无表单！'
        return json.dumps(ret)

    if 'status' not in data or 'mobile' not in data or 'old_password' not in data or 'new_password' not in data or 'job' not in data:
        ret['status']='error:表单缺失！'
        return json.dumps(ret)
    status = data['status']
    phonenumber = data['mobile']
    old_password = data['old_password']
    new_password = data['new_password']
    job = data['job']
    if not status or not phonenumber or not old_password or not new_password or not job:
        ret['status']='error:输入信息缺失！'
        return json.dumps(ret)
    if status=="" or phonenumber=="" or old_password=="" or new_password=="":
        ret['status']='error:输入信息为空！'
        return json.dumps(ret)
    if old_password == new_password:
        ret['status']='error:新密码与原密码相同！'
        return json.dumps(ret)

    if job == 'teacher':
        teacher = Teachers.query.filter_by(phonenumber = phonenumber).first()
        if teacher is None:
            ret['status']='error:该用户不存在！'
            return json.dumps(ret)
        if old_password != teacher.password:
            ret['status']='error:原密码错误！'
            return json.dumps(ret)
        else:
            teacher.password = new_password
            db.session.add(teacher)
            db.session.commit()
    elif job == 'student':
        student = Students.query.filter_by(phonenumber = phonenumber).first()
        if student is None:
            ret['status']='error:该用户不存在！'
            return json.dumps(ret)
        if old_password != student.password:
            ret['status']='error:原密码错误！'
            return json.dumps(ret)
        else:
            student.password = new_password
            db.session.add(student)
            db.session.commit()
    else:
        ret['status']='error:请选择学生或教师！'
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#Change_mobile
@user.route('/change_mobile', methods = ['POST'])
def change_mobile():
    ret = {}
    ret['status'] = 'error'

    text = request.get_data()
    print (text)
    if text:
        data = json.loads(text)
    else:
        ret['status']='error:无表单！'
        return json.dumps(ret)

    if 'status' not in data or 'old_mobile' not in data or 'old_verification' not in data or 'new_mobile' not in data or 'new_verification' not in data or 'job' not in data:
        ret['status']='error:表单缺失！'
        return json.dumps(ret)
    status = data['status']
    old_mobile = data['old_mobile']
    old_verification = data['old_verification']
    new_mobile = data['new_mobile']
    new_verificaiton = data['new_verification']
    job = data['job']
    if not status or not old_mobile or not old_verification or not new_mobile or not new_verificaiton or not job:
        ret['status']='error:输入信息缺失！'
        return json.dumps(ret)
    if status=="" or old_mobile=="" or old_verification=="" or new_mobile=="" or new_verificaiton=="" or job=="":
        ret['status']='error:输入信息为空！'
        return json.dumps(ret)
    if old_mobile == new_mobile:
        ret['status']='error:新手机号与原号码相同！'
        return json.dumps(ret)

    old_mess = Messages.query.filter_by(phonenumber = old_mobile).first()
    new_mess = Messages.query.filter_by(phonenumber = new_mobile).first()
    if old_mess is None or new_mess is None:
        ret['status']='error:请先发送短信验证码！'
        return json.dumps(ret)
    if old_verification != old_mess.message:
        print ('Not equal:' + old_verification + ' !=  ' + old_mess.message)
        ret['status']='error:原手机短信验证码错误！'
        return json.dumps(ret)
    elif new_verificaiton != new_mess.message:
        ret['status']='error:新手机短信验证码错误！'
        print ('Not equal:' + new_verification + ' !=  ' + new_mess.message)
        return json.dumps(ret)
    else:
        print ('Both equal!')
    db.session.delete(old_mess)
    db.session.delete(new_mess)
    db.session.commit()
    
    if job == 'teacher':
        teacher = Teachers.query.filter_by(phonenumber = old_mobile).first()
        if teacher is None:
            ret['status']='error:用户不存在！'
            return json.dumps(ret)
        teacher.phonenumber = new_mobile
        db.session.add(teacher)
        db.session.commit()
    elif job == 'student':
        student = Students.query.filter_by(phonenumber = old_mobile).first()
        if student is None:
            ret['status']='error:用户不存在！'
            return json.dumps(ret)
        student.phonenumber = new_mobile
        db.session.add(student)
        db.session.commit()
    else:
        ret['status']='error:请选择学生或教师！'
        return json.dumps(ret)

    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)
