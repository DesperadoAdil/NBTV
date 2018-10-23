# -*- coding: UTF-8 -*-
from flask import *
import json
from . import classroom
from ..polyv import polyvAPI
from .Classroom import classroomManager
from ..user.User import usermanager


polyvManager = polyvAPI.ChannelManager()

@classroom.route('/add_class')
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
	return ret


@classroom.route('/delete_class')
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
		return {"status": "error polyv"}

	#在教室列表中删除教室
	ret = {}
	ret['status'] = classroomManager.delete(data['url'])
	return ret


@classroom.route('/update_class')
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
