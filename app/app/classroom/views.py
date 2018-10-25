# -*- coding: UTF-8 -*-
from flask import *
import json
from . import classroom
from ..polyv import polyvAPI
from .Classroom import classroomManager
from ..user.User import usermanager


polyvManager = polyvAPI.ChannelManager()

@classroom.route('/add_class', methods = ['POST'])
def addClass():

	data = request.get_data()
	print('add a class')
	print(data)
	data = json.loads(data)

	if not usermanager.verify(data['username'], data['password'], "teacher"):
		return {"status": "error:password wrong"}


	#在保利威视创建一个直播频道
	response = polyvManager.createChannel(data['title'])

	if not response.status == 200:
		print('polyv make a mistake')

	responseData = json.loads(response.data.decode('utf8'))
	vid = responseData['data']['channelId']
	rtmpUrl = responseData['data']['url']

	# 在教室列表里插入一个教室
	# insert(self, vid, rtmpUrl, teacher, title, thumbnail, passwd, url):
	ret = {}
	ret['status'] = classroomManager.insert(vid, rtmpUrl, data['username'], data['title'], data['thumbnail'], data['class_password'], data['url'])
	
	# 在教师的教室列表中插入教室
	try:
		teacher = usermanager.search("username", data["username"], "teacher")
		cljson = json.loads(teacher.classroomlist)
		cljson.append(data['url'])
		teacher.classroomlist = json.dumps(cljson)
		db.session.add(teacher)
		db.session.commit()
	except Exception as err:
		print(err)
		ret['status'] = "error: no such teacher or classroom"

	return ret


@classroom.route('/delete_class', methods = ['POST'])
def deleteClass():
	data = request.get_data()
	print('delete a class')
	print(data)
	data = json.loads(data)

	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		return {"status": "error:password wrong"}

	classroomTmp = classroomManager.search(data['url'])
	if classroomTmp is None:
		return {"status": "error:no such classroom"}

	#从保利威视那删除这个直播频道
	response = polyvManager.deleteChannel(classroomTmp.vid)
	responseData = json.loads(response.data.decode('utf8'))
	if responseData['status'] == "error":
		return {"status": "error: polyv"}

	#在教室列表中删除教室
	ret = {}
	ret['status'] = classroomManager.delete(data['url'])

	#从教师的教室列表中删除教室
	try:
		teacher = usermanager.search("username", data['username'], "teacher")
		cljson = json.loads(teacher.classroomlist)
		cljson.remove(data['url'])
		teacher.classroomlist = json.dumps(cljson, ensure_ascii = False)
		db.session.add(teacher)
		db.session.commit()
	except Exception as err:
		print(err)
		ret['status'] = "error: no such teacher or classroom"

	return ret


@classroom.route('/update_class', methods = ['POST'])
def updateClass():
	data = request.get_data()
	print('update a classroom')
	print(data)
	data = json.loads(data)

	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		return {"status": "error:no such classroom"}

	ret = {}
	# update(self, title, thumbnail, newUrl, passwd, oldUrl):
	ret['status'] = classroomManager.update(data['title'], data['thumbnail'], data['url'], data['class_password'], data['old_url'])
	return ret

@classroom.route('/user_living_list', methods = ['POST'])
def getList():
	data = request.get_data()
	print('get the classroomList')
	print(data)
	data = json.loads(data)

	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		return {"status": "error:no such classroom"}

	ret = {}
	l = json.loads(usermanager.search("username", data["username"], "teacher").classroomlist)
	ans = []
	for v in l:
		tmp = classroomManager.search(v)
		tmpd = {"title": tmp.title, "thumbnail": tmp.thumbnail, "url": tmp.url, "password": tmp.password}
		ans.append(tmpd)
	return json.dumps(ans, ensure_ascii = False)








