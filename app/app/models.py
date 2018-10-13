from app import db

class Classrooms(db.Model):
    __tablename__ = 'classrooms'
    id = db.Column(db.Integer, primary_key=True,  unique=True, nullable=False)
    teacher = db.Column(db.String(50), db.ForeignKey('teachers.username'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), unique=True, nullable=False)
    studentlist = db.Column(db.String(1000), nullable=False)
    teacherlist = db.Column(db.String(1000), nullable=False)
    audiencelist = db.Column(db.String(1000), nullable=False)
    visible = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return '<ClassroomID %r>' % self.id


class Teachers(db.Model):
    __tablename__ = 'teachers'
    phonenumber = db.Column(db.String(11), primary_key=True,  unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.String(1000), nullable=False)
    classroom = db.relationship('Classrooms', backref='teachers', lazy='dynamic')

    def __repr__(self):
        return '<PhoneNumber %r>' % self.phonenumber


class Students(db.Model):
    __tablename__ = 'students'
    phonenumber = db.Column(db.String(11), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    classroomlist = db.Column(db.String(1000), nullable=False)

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

	def __repr__(self):
		return '<choiceQuestionId %r>' % self.choiceQuestionId


