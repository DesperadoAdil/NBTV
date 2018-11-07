# -*- coding: UTF-8 -*-
from flask import *
from app import app, socketio
from flask_socketio import join_room, leave_room, emit, send
from sqlalchemy import and_, or_, not_
from app.textMessage import TextMessage
from .models import *
import json, os
import random

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#Display_pdf
@app.route('/display', methods = ['GET', 'POST'])
def dispolay():
    return render_template("displaypdf.html")


#get pdf file
@app.route('/pdf/<path>')
def getPDF(path):
    return send_from_directory('/mnt/NBTV', path)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


@socketio.on('connect')
def test_connect():
    #print (data.get('username') + " connected.")
    print('Client connected')
    emit('open')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join')
def on_join(data):
    print ('join!')
    username = data.get('username')
    room = data['url']
    join_room(room)
    send(username + ' has entered the classroom.', room=room)


@socketio.on('sendMsg')
def sendmsg(data):
    print (data)
    type = data['type']
    if type == "broadcast":
        room = data['url']
        emit('broadcast', data, room=room)
    elif type == "whisper":
        username = data.get('toUser')
        emit('to'+username, data)
