from app.test.BaseTestCase import BaseTestCase
from app.models import *
from app.classroom.Classroom import classroomManager
import unittest
import json

class UserTest(BaseTestCase):
	data_login = { "username" : 'testuser', "password" : '654321', "job" : "teacher", "loginway" : "username" }
	dataerror_login = { "username" : '17799163762', "password" : '123456', "job" : "teacher", "loginway" : "phonenumber" }

	def test_login(self):
		print ("Test:Login===============================")

		# 这是不可以正确登录的结果
		response = self.app.post('/api/user/login', data = json.dumps(self.dataerror_login, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: wrong username or password"}')

		# 这是可以正确登录的结果
		response = self.app.post('/api/user/login', data = json.dumps(self.data_login, ensure_ascii = False))
		ret = json.loads(response.data.decode('utf8'))
		self.assertEquals(ret["status"], "success")
		testuser = Teachers.query.filter_by(username = "testuser").first()
		db.session.delete(testuser)
		db.session.commit()


	data_register = { "username" : 'testuser', "mobile" : "17799163761", "password" : '123456', "verification" : "123456", "job" : "teacher" }
	dataerror_register = { "username" : 'testuser', "mobile" : "17799163761", "password" : '123456', "verification" : "123456", "job" : "teacher" }

	def test_aregister(self):
		print ("Test:Register===============================")
		Message = Messages.query.filter_by(phonenumber = "17799163761").first()
		if Message is None:
			Message = Messages(phonenumber = "17799163761", message = "123456")
		else:
			Message.message = "123456"
		db.session.add(Message)
		db.session.commit()

		# 这是可以正确注册的结果
		response = self.app.post('/api/user/register', data = json.dumps(self.data_register, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确注册的结果
		response = self.app.post('/api/user/register', data = json.dumps(self.dataerror_register, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: please send textMessage first"}')

		message = Messages(phonenumber = "17799163761", message = "654321")
		db.session.add(message)
		db.session.commit()
		response = self.app.post('/api/user/register', data = json.dumps(self.dataerror_register, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: wrong textMessage"}')

		self.dataerror_register["verification"] = "654321"
		response = self.app.post('/api/user/register', data = json.dumps(self.dataerror_register, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: user already exist"}')


	data_change_password = { "status" : "login", "mobile" : "17799163761", "old_password" : "123456", "new_password" : "654321", "job" : 'teacher' }
	dataerror_change_password = { "status" : "logout", "mobile" : "12345678910", "old_password" : "654321", "new_password" : "654321", "job" : 'teacher' }

	def test_bchange_password(self):
		print ("Test:Change_password===============================")
		# 这是不可以正确修改密码的结果
		response = self.app.post('/api/user/change_password', data = json.dumps(self.dataerror_change_password, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: user does not login"}')

		self.dataerror_change_password["status"] = "login"
		response = self.app.post('/api/user/change_password', data = json.dumps(self.dataerror_change_password, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: user does not exist"}')

		self.dataerror_change_password["mobile"] = "17799163761"
		response = self.app.post('/api/user/change_password', data = json.dumps(self.dataerror_change_password, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: wrong old_password"}')

		# 这是可以正确修改密码的结果
		response = self.app.post('/api/user/change_password', data = json.dumps(self.data_change_password, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')


	data_change_mobile = { "status" : "login", "old_mobile" : "17799163761", "old_verification" : "123456", "new_mobile" : "17799163762", "new_verification" : "123456", "job" : "teacher" }
	dataerror_change_mobile = { "status" : "logout", "old_mobile" : "12345678911", "old_verification" : "654321", "new_mobile" : "17799163762", "new_verification" : "654321", "job" : "teacher" }

	def test_change_mobile(self):
		print ("Test:Change_mobile===============================")
		Message = Messages.query.filter_by(phonenumber = "12345678910").first()
		if Message is None:
			Message = Messages(phonenumber = "12345678910", message = "123456")
		else:
			Message.message = "123456"
		db.session.add(Message)
		db.session.commit()

		Message = Messages.query.filter_by(phonenumber = "17799163762").first()
		if Message is None:
			Message = Messages(phonenumber = "17799163762", message = "123456")
		else:
			Message.message = "123456"
		db.session.add(Message)
		db.session.commit()

		# 这是不可以正确修改手机号的结果
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.dataerror_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: user does not login"}')

		self.dataerror_change_mobile["status"] = "login"
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.dataerror_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: please send textMessage first"}')

		self.dataerror_change_mobile["old_mobile"] = "12345678910"
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.dataerror_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: wrong old_verification"}')

		self.dataerror_change_mobile["old_verification"] = "123456"
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.dataerror_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: wrong new_verification"}')

		self.dataerror_change_mobile["new_verification"] = "123456"
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.dataerror_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: user does not exist"}')

		Message = Messages.query.filter_by(phonenumber = "17799163761").first()
		if Message is None:
			Message = Messages(phonenumber = "17799163761", message = "123456")
		else:
			Message.message = "123456"
		db.session.add(Message)
		db.session.commit()

		Message = Messages.query.filter_by(phonenumber = "17799163762").first()
		if Message is None:
			Message = Messages(phonenumber = "17799163762", message = "123456")
		else:
			Message.message = "123456"
		db.session.add(Message)
		db.session.commit()

		# 这是可以正确修改手机号的结果
		response = self.app.post('/api/user/change_mobile', data = json.dumps(self.data_change_mobile, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')


	data_mylist = { "username" : "stu1", "job" : "student" }
	dataerror_mylist = { "username" : "stu1", "job" : "student" }

	def test_mylist(self):
		print ("Test:Mylist===============================")
		classroom = Classrooms.query.filter_by(url = "242544").first()
		dict = classroomManager.dict(classroom)
		ret = json.dumps([dict])

		# 这是可以正确获取直播间列表的结果
		response = self.app.post('/api/user/mylist', data = json.dumps(self.data_mylist, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), ret)


	testuser = Students(phonenumber = "12345678910", username = "testuser", password = "123456", classroomlist = json.dumps(["242544"]))
	db.session.add(testuser)
	Classroom = classroomManager.search("242544")
	classroomuser = json.loads(Classroom.studentlist)
	classroomuser.append("testuser")
	Classroom.studentlist = json.dumps(classroomuser)
	db.session.add(Classroom)
	db.session.commit()
	classroom = classroomManager.dict(Classroom)
	classroom["url"] = "123456"
	data_delmyclass = { "username" : "testuser", "job" : "student", "classroom" : classroom }
	dataerror_delmyclass = { "username" : "stu2", "job" : "student", "classroom" : classroom }

	def test_ndelmyclass(self):
		print ("Test:Delmyclass===============================")

		# 这是不可以正确删除直播间列表的结果
		response = self.app.post('/api/user/delmyclass', data = json.dumps(self.dataerror_delmyclass, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error"}')

		# 这是可以正确删除直播间列表的结果
		self.classroom["url"] = "242544"
		response = self.app.post('/api/user/delmyclass', data = json.dumps(self.data_delmyclass, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')
		testuser = Students.query.filter_by(username = "testuser").first()
		db.session.delete(testuser)
		db.session.commit()


	open_close_live_data = {
		"username": "adil",
		"url": "123456"
	}
	def test_open_close_live(self):
		print("test: open and close live")

		response = self.app.post('/api/user/openliving', json.dumps(self.open_close_live_data))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")

		response = self.app.post('/api/user/closeliving', json.dumps(self.open_close_live_data))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")

