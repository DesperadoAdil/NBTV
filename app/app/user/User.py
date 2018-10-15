from ..models import *
import json

class UserManager:
    def __init__(self):
        pass

    def insert(self, phonenumber, username, password, job):
        try:
            if job == "teacher":
                teacher = Teachers(phonenumber=phonenumber, username=username, password=password, classroomlist="[]")
                db.session.add(teacher)
            elif job == "student":
                student = Students(phonenumber=phonenumber, username=username, password=password, classroomlist="[]")
                db.session.add(student)
            else:
                print ("Insert Error: Database Not Found")
                return "error"
            db.session.commit()
            print ("success")
            return "success"
        except:
            print ("error")
            return "error"

    def update(self, user, phonenumber, username, password, classroomlist):
        try:
            user.phonenumber = phonenumber
            user.username = username
            user.password = password
            user.classroomlist = classroomlist
            db.session.add(user)
            db.session.commit()
            return "success"
        except:
            return "error"

    def search(self, searchmode, key, job):
        if job == "teacher":
            if searchmode == "phonenumber":
                teacher = Teachers.query.filter_by(phonenumber = key).first()
            elif searchmode == "username":
                teacher = Teachers.query.filter_by(username = key).first()
            if teacher is None:
                print ("Search Error: Teacher Not Found")
            return teacher
        elif job == "student":
            if searchmode == "phonenumber":
                student = Students.query.filter_by(phonenumber = key).first()
            elif searchmode == "username":
                student = Students.query.filter_by(username = key).first()
            if student is None:
                print ("Search Error: Student Not Found")
            return student
        else:
            print ("Insert Error: Database Not Found")
            return None

    def delete(self, user):
        try:
            db.session.delete(user)
            db.session.commit()
            return "success"
        except:
            return "error"

usermanager = UserManager()
