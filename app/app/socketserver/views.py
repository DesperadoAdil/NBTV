from flask_socketio import join_room, leave_room, emit, send
from .. import socketio
from ..models import *
import json

chatingRoom = {}

@socketio.on('connect')
def test_connect():
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
	send(username + '进入房间。', room = url, include_self = False)

	if url not in chatingRoom.keys():
		chatingRoom[url] = []
	if username not in chatingRoom[url]:
		chatingRoom[url].append(username)

	classroom = Classrooms.query.filter_by(url = url).first()
	if classroom is not None:
		obj = json.loads(classroom.status)
		if 'type' in obj:
			typee = obj['type']
			if typee == "pdf":
				emit('pdf', obj, room = username)
			elif typee == "page":
				emit('page', obj, room = username)
			elif typee == "code":
				emit('code', obj, room = username)
			elif typee == "select":
				emit('select', obj, room = username)
			elif typee == "close":
				emit('close', obj, room = username)


@socketio.on('sendMsg')
def sendMsg(data):
	print (data)
	type = data['type']
	if type == "broadcast":
		emit('broadcast', data, room = data['url'])
	elif type == "whisper":
		emit('whisper', data, room = data['fromUser'])
		emit('whisper', data, room = data['toUser'])
	elif type == "pdf":
		emit('pdf', data, room = data['url'])
		classroom = Classrooms.query.filter_by(url = data['url']).first()
		classroom.status = json.dumps(data)
		db.session.add(classroom)
		db.session.commit()
	elif type == "page":
		emit('page', data, room = data['url'])
		classroom = Classrooms.query.filter_by(url = data['url']).first()
		classroom.status = json.dumps(data)
		db.session.add(classroom)
		db.session.commit()
	elif type == "code":
		emit('code', data, room = data['url'])
		classroom = Classrooms.query.filter_by(url = data['url']).first()
		classroom.status = json.dumps(data)
		db.session.add(classroom)
		db.session.commit()
	elif type == "select":
		emit('select', data, room = data['url'])
		classroom = Classrooms.query.filter_by(url = data['url']).first()
		classroom.status = json.dumps(data)
		db.session.add(classroom)
		db.session.commit()
	elif type == "close":
		emit('close', data, room = data['url'])
		classroom = Classrooms.query.filter_by(url = data['url']).first()
		classroom.status = json.dumps(data)
		db.session.add(classroom)
		db.session.commit()


@socketio.on('list')
def list(data):
	url = data['url']
	emit('list', chatingRoom[url], room = data['username'])


@socketio.on('refresh')
def refresh(data):
	chatingRoom[data['url']].clear()
	emit('check', room = data['url'])


@socketio.on('check')
def check(data):
	print ("check!")
	chatingRoom[data['url']].append(data['username'])


@socketio.on('blacklist')
def blacklist(data):
	print ("BlackList!")
	username = data["toUser"]
	url = data["url"]

	classroom = Classrooms.query.filter_by(url = url).first()
	blacklist = json.loads(classroom.blacklist)
	if username not in blacklist:
		blacklist.append(username)
	classroom.blacklist = json.dumps(blacklist)
	if classroom.mode is "private":
		studentlist = json.loads(classroom.studentlist)
		if username in studentlist:
			studentlist.remove(username)
		classroom.studentlist = json.dumps(studentlist)
	db.session.add(classroom)
	db.session.commit()

	emit('blacklist', room = username)


@socketio.on('shutup')
def shutup(data):
	print ("ShutupList!")
	username = data["toUser"]
	url = data["url"]

	classroom = Classrooms.query.filter_by(url = url).first()
	shutuplist = json.loads(classroom.shutuplist)
	if username not in shutuplist:
		shutuplist.append(username)
	classroom.shutuplist = json.dumps(shutuplist)
	db.session.add(classroom)
	db.session.commit()

	emit('shutup', room = username)


@socketio.on('noShutUp')
def noShutUp(data):
	print ("You Can Talk!")
	username = data['username']
	url = data['url']
	#print (username, url)

	classroom = Classrooms.query.filter_by(url = url).first()
	shutuplist = json.loads(classroom.shutuplist)
	if username in shutuplist:
		shutuplist.remove(username)
	classroom.shutuplist = json.dumps(shutuplist)
	db.session.add(classroom)
	db.session.commit()

	emit('noShutUp', room = username)

@socketio.on('clear')
def clear():
	chatingRoom.clear()
