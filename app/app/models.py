from app import db
from datetime import datetime

class Classrooms(db.Model):
    __tablename__ = 'classrooms'
    __table_args__ = {
        'mysql_charset':'utf8'
    }
    # id = db.Column(db.Integer, primary_key=True,  unique=True, nullable=False)
    vid = db.Column(db.Integer, unique=True, nullable=False)
    teacher = db.Column(db.String(50), db.ForeignKey('teachers.username'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False)
    #直播间私密模式
    mode = db.Column(db.String(10), nullable=False, default="private")

    #直播间的密码
    password = db.Column(db.String(50), nullable=False)

    #直播间的url
    url = db.Column(db.String(100), unique=True, nullable=False, primary_key = True)

    # 推流的地址
    rtmpUrl = db.Column(db.String(133), unique = True, nullable = False)

    studentlist = db.Column(db.Text, nullable=False, default = "[]")
    teacherlist = db.Column(db.Text, nullable=False, default = "[]")
    #audiencelist = db.Column(db.Text, nullable=False, default = "[]")

    filelist = db.Column(db.Text, nullable = False, default = "[]")

    visible = db.Column(db.String(5), nullable=False, default = "yes")
    createtime = db.Column(db.DateTime, default=datetime.now())
    #开播时间
    showtime = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # choicequestion = db.relationship('ChoiceQuestion', backref='classrooms', lazy='dynamic')
    # codequestion = db.relationship('CodeQuestion', backref='classrooms', lazy='dynamic')

    def __repr__(self):
        return '<ClassroomUrl %r>' % self.url


class Teachers(db.Model):
    __tablename__ = 'teachers'
    __table_args__ = {
        'mysql_charset':'utf8'
    }
    phonenumber = db.Column(db.String(11), unique=True, nullable=False)
    username = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.Text, nullable=False, default = "[]")
    
    classroom = db.relationship('Classrooms', backref='teachers', lazy='dynamic')
    
    pdfs = db.relationship('PDFFile', backref = "teachers", lazy = "dynamic")
    codeQue = db.relationship('CodeQuestion', backref = "teachers", lazy = "dynamic")
    choiceQue = db.relationship('ChoiceQuestion', backref = "teachers", lazy = "dynamic")

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber


class Students(db.Model):
    __tablename__ = 'students'
    __table_args__ = {
        'mysql_charset':'utf8'
    }
    phonenumber = db.Column(db.String(11), unique=True, nullable=False)
    username = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.Text, nullable=False, default = "[]")

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber


class Messages(db.Model):
    __tablename__ = 'messages'
    __table_args__ = {
        'mysql_charset':'utf8'
    }
    phonenumber = db.Column(db.String(11), primary_key=True, unique=True, nullable=False)
    message = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber

class ChoiceQuestion(db.Model):
    __tablename__ = 'choicequestion'
    __table_args__ = {
        'mysql_charset':'utf8'
    }
    statement = db.Column(db.String(1000), nullable = False)
    optionList = db.Column(db.String(1000), nullable = False)
    answer = db.Column(db.Integer, nullable = False)
    uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
    submitRecord = db.Column(db.Text, nullable = False)
    # classroom = db.Column(db.String(100), db.ForeignKey('classrooms.url', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    owner = db.Column(db.String(50), db.ForeignKey('teachers.username', ondelete = "CASCADE", onupdate = "CASCADE"), nullable = False)
    
    def __repr__(self):
        return '<choiceQuestionId %r>' % self.choiceQuestionId


class CodeQuestion(db.Model):
    __tablename__ = 'codequestion'
    __table_args__ = { 'mysql_charset':'utf8' }
    statement = db.Column(db.String(1000), nullable = False)
    language = db.Column(db.String(10), nullable = False)
    uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
    submitRecord = db.Column(db.Text, nullable = False)
    # classroom = db.Column(db.String(100), db.ForeignKey('classrooms.url', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    owner = db.Column(db.String(50), db.ForeignKey('teachers.username', ondelete = "CASCADE", onupdate = "CASCADE"), nullable = False)

    def __repr__(self):
        return '<codequestionId %r>' % self.uniqueId

class PDFFile(db.Model):
    __tablename__ = 'pdffile'

    # uniqueId = db.Column(db.String(10), primary_key = True, unique = True, nullable = False)
    owner = db.Column(db.String(50), db.ForeignKey('teachers.username', ondelete = "CASCADE", onupdate = "CASCADE"), nullable = False)
    filename = db.Column(db.String(100), nullable = False)
    uniqueId = db.Column(db.String(151), nullable = False, primary_key = True)
    # filePath = db.Column(db.Text, nullable = False)
    __table_args__ = (
        db.Index('filepath', 'owner', 'filename'),
        {'mysql_charset':'utf8'}
    )

    def __repr__(self):
        return '<pdfId %r>' % self.owner
