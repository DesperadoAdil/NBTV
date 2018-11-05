# -*- coding: UTF-8 -*-
from flask import *
import json
from . import classroom
from ..polyv import polyvAPI
from .Classroom import *
from ..user.User import usermanager
from ..models import Classrooms


polyvManager = polyvAPI.ChannelManager()

@classroom.route('/add_class', methods = ['POST'])
def addClass():
	ret = {}
	data = request.get_data()
	print('add a class')
	print(data)
	data = json.loads(data)
	try:
		if not usermanager.verify(data['username'], data['password'], "teacher"):
			ret["status"] = "error:password wrong"
			return json.dumps(ret, ensure_ascii = False)
	except Exception as err:
		print(err)
		ret['status'] = "error"
		return json.dumps(ret, ensure_ascii = False)

	#在保利威视创建一个直播频道
	response = polyvManager.createChannel(data['title'], data['class_password'])

	if not response.status == 200:
		print('polyv make a mistake')
		print(response.data.decode("utf8"))
		ret["status"] = "error: polyv has been error"
		return json.dumps(ret, ensure_ascii = False)

	responseData = json.loads(response.data.decode('utf8'))
	vid = responseData['data']['channelId']
	rtmpUrl = responseData['data']['url']

	# 在教室列表里插入一个教室
	# insert(self, vid, rtmpUrl, teacher, title, thumbnail, passwd, url):
	ret = {}
	ret['status'] = classroomManager.insert(vid, rtmpUrl, data['username'], data['title'], data['thumbnail'], data['class_password'], data['url'], data['mode'])

	return json.dumps(ret, ensure_ascii = False)


@classroom.route('/delete_class', methods = ['POST'])
def deleteClass():
	data = request.get_data()
	print('delete a class')
	print(data)
	data = json.loads(data)

	ret = {}

	if not usermanager.verify(data['username'], data['password'], 'teacher'):

		ret["status"] = "error:password wrong"
		return json.dumps(ret, ensure_ascii = False)

	classroomTmp = classroomManager.search(data['url'])
	if classroomTmp is None:
		ret["status"] = "error:no such classroom"
		return json.dumps(ret, ensure_ascii = False)

	#从保利威视那删除这个直播频道
	response = polyvManager.deleteChannel(classroomTmp.vid)
	responseData = json.loads(response.data.decode('utf8'))
	if responseData['status'] == "error":
		ret["status"] = "error: polyv"
		return json.dumps(ret, ensure_ascii = False)

	#从直播间观众的观看列表中删除教室
	try:
		teacherlist = json.loads(classroomTmp.teacherlist)
		for teachername in teacherlist:
			teacher = usermanager.search("username", teachername, "teacher")
			classroomlist = json.loads(teacher.classroomlist)
			classroomlist.remove(data['url'])
			teacher.classroomlist = json.dumps(classroomlist)
			db.ssesion.add(teacher)

		studentlist = json.loads(classroomTmp.studentlist)
		for studentname in studentlist:
			student = usermanager.search("username", studentname, "student")
			classroomlist = json.loads(student.classroomlist)
			classroomlist.remove(data['url'])
			student.classroomlist = json.dumps(classroomlist)
			db.ssesion.add(student)
		db.session.commit()
	except Exception as err:
		print(err.encode("utf-8"))
		ret['status'] = "error: no such teacher or classroom"

	ret['status'] = classroomManager.delete(data['url'])

	return json.dumps(ret, ensure_ascii = False)


@classroom.route('/update_class', methods = ['POST'])
def updateClass():
	data = request.get_data()
	print('update a classroom')
	print(data)
	data = json.loads(data)

	ret = {}
	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		ret["status"] = "error:password wrong"
		return json.dumps(ret, ensure_ascii = False)

	# update(self, title, thumbnail, newUrl, passwd, oldUrl):
	ret['status'] = classroomManager.update(data['title'], data['thumbnail'], data['url'], data['class_password'], data['old_url'])
	return json.dumps(ret, ensure_ascii = False)

@classroom.route('/user_living_list', methods = ['POST'])
def getList():
	data = request.get_data()
	print('get the classroomList')
	print(data)
	data = json.loads(data)

	ret = {}
	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		ret["status"] = "error:password wrong"
		return json.dumps(ret, ensure_ascii = False)

	l = usermanager.search("username", data["username"], "teacher").classroom
	#l = Classrooms.query.filter(Classrooms.teacher == data['username']).all()
	ans = []
	for tmp in l:
		tmpd = {"title": tmp.title, "thumbnail": tmp.thumbnail, "url": tmp.url, "password": tmp.password}
		ans.append(tmpd)
	return json.dumps(ans, ensure_ascii = False)
