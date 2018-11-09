# -*- coding: UTF-8 -*-
from flask import *
from . import developer
from .forms import *
from ..models import *

@developer.route('/')
def base():
    return render_template("base.html")


#Add_user
@developer.route('/add_user', methods = ['GET', 'POST'])
def add_user():
    form = UserForm()

    if request.method == 'GET':
        return render_template("developer.html", form = form)
    else:
        form = UserForm(formdata=request.form)
        if form.validate():
            phonenumber = form.data['phonenumber']
            if form.data['user'] == 1:
                student = Students.query.filter_by(phonenumber = phonenumber).first()
                if student is None:
                    student = Students(phonenumber=form.data['phonenumber'], username=form.data['username'], password=form.data['password'], classroomlist="[]")
                    db.session.add(student)
                    db.session.commit()
                    return render_template("base.html")
                else:
                    print ('User already exist!')
            else:
                teacher = Teachers.query.filter_by(phonenumber = phonenumber).first()
                if teacher is None:
                    teacher = Teachers(phonenumber=form.data['phonenumber'], username=form.data['username'], password=form.data['password'], classroomlist="[]")
                    db.session.add(teacher)
                    db.session.commit()
                    return render_template("base.html")
                else:
                    print ('User already exist!')
        else:
            print(form.errors)
    return render_template("developer.html", form = form)


#Add_classroom
@developer.route('/add_classroom', methods = ['GET', 'POST'])
def add_classroom():
    form = ClassForm()

    if request.method == 'GET':
        return render_template("developer.html", form = form)
    else:
        form = ClassForm(formdata=request.form)
        if form.validate():
            url = int(form.data['url'])
            classroom = Classrooms.query.filter_by(url = url).first()
            if classroom is None:
                classroom = Classrooms(vid=form.data['vid'], teacher=form.data['teacher'], title=form.data['title'], thumbnail=form.data['thumbnail'], password=form.data['password'], url=form.data['url'], visible=form.data['visible'], mode=form.data['mode'])
                db.session.add(classroom)
                db.session.commit()
                return render_template("base.html")
            else:
                    print ('Classroom already exist!')
        else:
            print(form.errors)
    return render_template("developer.html", form = form)
