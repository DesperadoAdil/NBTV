from flask import request
from flask_socketio import join_room, leave_room, emit, send
from . import socketserver
from .. import socketio
import json

url = '/242544'

@socketio.on('connect')
def on_connect():
    print ('Client connected')
    emit('open')


@socketio.on('disconnect')
def test_disconnect():
    print ('Client disconnected')


@socketio.on('join')
def on_join(data):
    print ('join!')
    username = data['username']
    url = data['url']
    join_room(username)
    join_room(url)
    send(username + ' has entered the classroom.', room = url)


@socketio.on('sendMsg')
def sendMsg(data):
    print (data)
    type = data['type']
    if type == "broadcast":
        emit('broadcast', data, room = data['url'])
    elif type == "whisper":
        emit('whisper', data, room = data['username'])
