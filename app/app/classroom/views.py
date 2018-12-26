# -*- coding: UTF-8 -*-
from flask import *
import json
from . import classroom
from ..polyv import polyvAPI
from .Classroom import *
from ..user.User import usermanager
from ..models import Classrooms
import xlrd
from os.path import join
from tempfile import mkdtemp
from shutil import rmtree


polyvManager = polyvAPI.ChannelManager()

@classroom.route('/add_class', methods = ['POST'])
def addClass():
	ret = {}
	data = request.form.to_dict()
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

	# 把缩略图给存起来
	imgfile = request.files.get('img')


	# 在教室列表里插入一个教室
	# insert(self, vid, rtmpUrl, teacher, title, thumbnail, passwd, url):
	ret = {}
	ret['status'] = classroomManager.insert(vid, rtmpUrl, data['username'], data['title'], imgfile, data['class_password'], data['url'], data['mode'])

	if ret['status'] != "success":
		polyvManager.deleteChannel(vid)

	return json.dumps(ret, ensure_ascii = False)


@classroom.route('/delete_class', methods = ['POST'])
def deleteClass():
	data = request.get_data()
	print('delete a class')
	#print(data)
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
			db.session.add(teacher)

		studentlist = json.loads(classroomTmp.studentlist)
		for studentname in studentlist:
			student = usermanager.search("username", studentname, "student")
			classroomlist = json.loads(student.classroomlist)
			classroomlist.remove(data['url'])
			student.classroomlist = json.dumps(classroomlist)
			db.session.add(student)
		db.session.commit()
	except Exception as err:
		print(err)
		ret['status'] = "error: no such teacher or classroom"

	ret['status'] = classroomManager.delete(data['url'])

	return json.dumps(ret, ensure_ascii = False)


@classroom.route('/update_class', methods = ['POST'])
def updateClass():
	data = request.form.to_dict()
	print('update a classroom')
	# print(data)

	ret = {}
	if not usermanager.verify(data['username'], data['password'], 'teacher'):
		ret["status"] = "error:password wrong"
		return json.dumps(ret, ensure_ascii = False)

	imgfile = request.files.get('img')
	# update(self, title, thumbnail, newUrl, passwd, oldUrl):
	ret['status'] = classroomManager.update(data['title'], imgfile, data['url'], data['class_password'], data['old_url'])
	return json.dumps(ret, ensure_ascii = False)


@classroom.route('/user_living_list', methods = ['POST'])
def getList():
	data = request.get_data()
	print('get the classroomList')
	#print(data)
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


@classroom.route('/getstudents', methods = ['POST'])
def getstudents():
	ret = []
	data = request.get_data()
	data = json.loads(data)
	url = data['url']
	classroom = classroomManager.search(url)
	if classroom is not None:
		ret = json.loads(classroom.studentlist)

	return json.dumps(ret)


@classroom.route('/urlcheck', methods = ['POST'])
def urlcheck():
	ret = {}
	data = request.get_data()
	data = json.loads(data)
	#print (data)
	url = data['url']
	username = data['username']
	classroom = classroomManager.search(url)
	if classroom is None:
		ret['status'] = "error"
		return json.dumps(ret)
	if classroom.mode == "public":
		ret['status'] = "success"
	elif classroom.mode == "protected":
		ret['status'] = "password"
		ret['password'] = classroom.password
	elif classroom.mode == "private":
		studentlist = json.loads(classroom.studentlist)
		if username in studentlist:
			ret['status'] = "success"
		else:
			ret['status'] = "error"
	else:
		ret['status'] = "error"
	return json.dumps(ret)


@classroom.route('/shutuplist', methods = ['POST'])
def shutuplist():
	data = request.get_data()
	data = json.loads(data)
	classroom = classroomManager.search(data['url'])
	return classroom.shutuplist


#xlsx添加学生
@classroom.route('/xlsxaddstudents', methods = ['POST'])
def xlsxaddstudents():
	ret = []
	data = request.form.to_dict()
	#print (data)

	url = data['url']
	item = request.files.get('item')
	tempdir = mkdtemp()
	filename = item.filename
	filepath = join(tempdir, filename)
	item.save(filepath)

	classroom = classroomManager.search(url)
	studentlist = json.loads(classroom.studentlist)

	workbook = xlrd.open_workbook(filepath)
	sheet_names = workbook.sheet_names()
	for sheet_name in sheet_names:
		sheet = workbook.sheet_by_name(sheet_name)
		rows = sheet.nrows
		cols = sheet.ncols
		for i in range(rows):
			for j in range(cols):
				user = sheet.cell_value(i, j)
				if user is None or user == "":
					continue
				if user in studentlist:
					#print ("Xlsx Add Student Error: " + user.encode('utf8') + " already in classroom")
					continue
				student = usermanager.search("username", user, "student")
				if student is None:
					#print ("Xlsx Add Student Error: " + user.encode('utf8') + " does not exist")
					continue

				#学生classroomlist中加入直播间url
				classroomlist = json.loads(student.classroomlist)
				classroomlist.append(url)
				student.classroomlist = json.dumps(classroomlist)
				db.session.add(student)

				#直播间studentlist中加入学生username
				studentlist.append(user)

				ret.append(user)

	classroom.studentlist = json.dumps(studentlist)
	db.session.add(classroom)
	db.session.commit()
	rmtree(tempdir)

	#print (json.dumps(ret))
	return json.dumps(ret)


#username添加学生
@classroom.route('/aaddstudents', methods = ['POST'])
def aaddstudents():
	ret = {}
	ret["status"] = 'error'

	data = request.get_data()
	data = json.loads(data)

	url = data['url']
	item = data['item']

	student = usermanager.search("username", item, "student")
	classroom = classroomManager.search(url)
	if student is None:
		#print ("Add Student Error: " + item.encode('utf8') + " does not exist")
		ret['status'] = 'error: no such student'
	elif classroom is None:
		#print ("Add Student Error: " + url.encode('utf8') + " does not exist")
		ret['status'] = 'error: no such classroom'
	else:
		#直播间studentlist中加入学生username
		studentlist = json.loads(classroom.studentlist)
		if item not in studentlist:
			studentlist.append(item)
			classroom.studentlist = json.dumps(studentlist)
			db.session.add(classroom)
			db.session.commit()
		else:
			#print ("Add Student Error: " + item.encode('utf8') + " already in classroom")
			pass

		#学生classroomlist中加入直播间url
		classroomlist = json.loads(student.classroomlist)
		if url not in classroomlist:
			classroomlist.append(url)
			student.classroomlist = json.dumps(classroomlist)
			db.session.add(student)
			db.session.commit()
		else:
			#print ("Add Student Error: " + item.encode('utf8') + " already in classroom")
			pass

		ret['status'] = "success"

	#print (json.dumps(ret))
	return json.dumps(ret)



@classroom.route('/openliving', methods = ['POST'])
def openlive():
	ret = {}
	ret["status"] = 'error'

	data = request.get_data()
	print('openlive')
	#print(data)

	data = json.loads(data)
	url = data['url']
	classroom = classroomManager.search(url)
	if classroom is None:
		ret['status'] = "error: no such classroom"
	else:
		ret['streamername'] = classroom.rtmpUrl
		ret['streamername'] = ret['streamername'].split('/')[-1]
		vid = classroom.vid
		response = polyvAPI.instance.openLive(vid)

		classroomManager.updateShowTime(url, "open")
		if response.status != 200:
			ret['status'] = "error: polyv error"
		else:
			ret['status'] = "success"

	#print (json.dumps(ret))
	return json.dumps(ret)


@classroom.route('/closeliving', methods = ['POST'])
def closelive():
	ret = {}
	ret["status"] = 'error'

	data = request.get_data()
	print('closelive')
	#print(data)

	data = json.loads(data)
	url = data['url']

	classroom = classroomManager.search(url)
	if classroom is None:
		ret['status'] = "error: no such classroom"
	else:
		vid = classroom.vid
		ret['vid'] = vid
		response = polyvAPI.instance.closeLive(vid)
		classroomManager.updateShowTime(url, "close")
		if response.status != 200:
			ret['status'] = "error: polyv error"
		else:
			classroom.status = json.dumps({'type': "closeliving"})
			db.session.add(classroom)
			db.session.commit()
			ret['status'] = "success"

	#print (json.dumps(ret))
	return json.dumps(ret)
