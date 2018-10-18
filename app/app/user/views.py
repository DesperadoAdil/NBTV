# -*- coding: UTF-8 -*-
from flask import *
from . import user
from sqlalchemy import and_, or_, not_
from ..textMessage import TextMessage
from ..models import *
import json
import random
from .User import usermanager

#Login
@user.route('/login', methods = ['POST'])
def login():
    ret = {}
    ret["status"] = 'error'
    
    data = request.get_data()
    print (data)
    data = json.loads(data)

    username = data['username']
    password = data['password']
    job = data['job']

    user = usermanager.search(data["loginway"], username, job)
    if user is None or password != user.password:
        ret['status']='error:用户名或密码错误！'
        return json.dumps(ret)
    print (job + ' login, username = ' + user.username)
    ret['username'] = user.username
    ret['password'] = user.password
    ret['rpassword'] = user.password
    ret['mobile'] = user.phonenumber
    ret['verification'] = ""
    ret['job'] = job
    ret['status'] = "success"
    print (json.dumps(ret))
    return json.dumps(ret)


#Register
@user.route('/register', methods = ['POST'])
def register():
    ret = {}
    ret["status"] = 'error'
    
    data = request.get_data()
    print (data)
    data = json.loads(data)

    phonenumber = data['mobile']
    username = data['username']
    password = data['password']
    job = data['job']
    verification = data['verification']

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

    user = usermanager.search("phonenumber", phonenumber, job)
    if user is not None:
        ret['status']='error:用户已存在！'
        return json.dumps(ret)
    ret['status'] = usermanager.insert(phonenumber, username, password, job)
    print (json.dumps(ret))
    return json.dumps(ret)


#Verification
@user.route('/request_verification', methods = ['POST'])
def verification():
    ret = {}
    ret["status"] = 'error'
    
    data = request.get_data()
    print (data)
    data = json.loads(data)

    phonenumber = data['mobile']
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
    
    data = request.get_data()
    print (data)
    data = json.loads(data)

    status = data['status']
    if status != "login":
        ret['status']='error:该用户未登录！'
        return json.dumps(ret)
    phonenumber = data['mobile']
    old_password = data['old_password']
    new_password = data['new_password']
    job = data['job']

    user = usermanager.search("phonenumber", phonenumber, job)
    if user is None:
        ret['status']='error:该用户不存在！'
        return json.dumps(ret)
    if old_password != user.password:
        ret['status']='error:原密码错误！'
        return json.dumps(ret)
    ret['status'] = usermanager.update(user, phonenumber, user.username, new_password, user.classroomlist)
    print (json.dumps(ret))
    return json.dumps(ret)


#Change_mobile
@user.route('/change_mobile', methods = ['POST'])
def change_mobile():
    ret = {}
    ret["status"] = 'error'
    
    data = request.get_data()
    print (data)
    data = json.loads(data)

    status = data['status']
    if status != "login":
        ret['status']='error:该用户未登录！'
        return json.dumps(ret)
    old_mobile = data['old_mobile']
    old_verification = data['old_verification']
    new_mobile = data['new_mobile']
    new_verificaiton = data['new_verification']
    job = data['job']

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

    user = usermanager.search("phonenumber", old_mobile, job)
    if user is None:
        ret['status']='error:用户不存在！'
        return json.dumps(ret)
    ret['status'] = usermanager.update(user, new_mobile, user.username, user.password, user.classroomlist)
    print (json.dumps(ret))
    return json.dumps(ret)
