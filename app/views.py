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
        return '{ status : error }'

    if job == 'teacher':
        teacher = Teachers.query.filter(and_(Teachers.username == username, Teachers.password == password)).first()
        if not teacher:
            return '{ status : error }'
    
    return '{ status : success }'
    

'''@app.route('/user/register', methods = ['POST'])
def register():
    
'''
