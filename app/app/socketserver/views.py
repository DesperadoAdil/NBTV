from flask_socketio import join_room, leave_room, emit, send
from .. import socketio

chatingRoom = {}

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

    if url not in chatingRoom.keys():
        chatingRoom[url] = []
    if username not in chatingRoom[url]:
        chatingRoom[url].append(username)


@socketio.on('sendMsg')
def sendMsg(data):
    type = data['type']
    if type == "broadcast":
        emit('broadcast', data, room = data['url'])
    elif type == "whisper":
        emit('whisper', data, room = data['username'])


@socketio.on('list')
def list(data):
    url = data['url']
    print ("send list :")
    print (chatingRoom[url])
    emit('list', chatingRoom[url], room = data['username'])


@socketio.on('refresh')
def refresh(data):
    chatingRoom[data['url']].clear()
    emit('check', room = data['url'])


@socketio.on('check')
def check(data):
    print ("check : ", data)
    chatingRoom[data['url']].append(data['username'])
    print (chatingRoom[data['url']])
