from app import db
from datetime import datetime

class Classrooms(db.Model):
    __tablename__ = 'classrooms'
    # id = db.Column(db.Integer, primary_key=True,  unique=True, nullable=False)
    vid = db.Column(db.Integer, unique=True, nullable=False)
    teacher = db.Column(db.String(50), db.ForeignKey('teachers.username'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), unique=True, nullable=False, primary_key = True)
    studentlist = db.Column(db.Text, nullable=False, default = "[]")
    teacherlist = db.Column(db.Text, nullable=False, default = "[]")
    audiencelist = db.Column(db.Text, nullable=False, default = "[]")
    visible = db.Column(db.String(5), nullable=False, default = "yes")
    createtime = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<ClassroomUrl %r>' % self.url


class Teachers(db.Model):
    __tablename__ = 'teachers'
    phonenumber = db.Column(db.String(11), primary_key=True,  unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.Text, nullable=False)
    classroom = db.relationship('Classrooms', backref='teachers', lazy='dynamic')

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber


class Students(db.Model):
    __tablename__ = 'students'
    phonenumber = db.Column(db.String(11), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber


class Messages(db.Model):
    __tablename__ = 'messages'
    phonenumber = db.Column(db.String(11), primary_key=True, unique=True, nullable=False)
    message = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber

class ChoiceQuestion(db.Model):
	__tablename__ = 'choicequestion'
	statement = db.Column(db.String(1000), nullable = False)
	optionList = db.Column(db.String(1000), nullable = False)
	answer = db.Column(db.Integer, nullable = False)
	uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
	submitRecord = db.Column(db.Text, nullable = False)


	def __repr__(self):
		return '<choiceQuestionId %r>' % self.choiceQuestionId


class CodeQuestion(db.Model):
	__tablename__ = 'codequestion'
	statement = db.Column(db.String(1000), nullable = False)
	language = db.Column(db.String(10), nullable = False)
	uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
	submitRecord = db.Column(db.Text, nullable = False)

	def __repr__(self):
		return '<codequestionId %r>' % self.uniqueId

class PDFFile(db.Model):
	__tablename__ = 'pdffile'
	uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
	filePath = db.Column(db.Text, nullable = False)

	def __repr__(self):
		return '<pdfId %r>' % self.uniqueId