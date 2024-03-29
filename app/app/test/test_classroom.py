from app.test.BaseTestCase import BaseTestCase
from app.models import *
import unittest
import json

class ClassroomTest(BaseTestCase):

	data = {
			"username": "adil",
			"password": "123456",
			"title": "adilnba!",
			"class_password": "121121",
			"thumbnail": "/static/image/test.jpg",
			"url": "123",
			"old_url": "123",
			"mode": "private"
		}

	dataerror = {
		"username": "adil",
		"password": "1234",
		"title": "adilnba!",
		"class_password": "121121",
		"thumbnail": "/static/image/test.jpg",
		"url": "123",
		"old_url": "123",
		"mode": "private"
	}

	def test_add_classroom(self):
		classroom = Classrooms.query.filter_by(url = "123").first()
		if classroom is not None:
			db.session.delete(classroom)
			db.session.commit()

		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = self.data)
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = self.dataerror)
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')


	def test_bupdate_classroom(self):
		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = self.data)
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = self.dataerror)
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')


	data_aaddstudents = { "url" : "123", "item" : "test1" }
	dataerror_aaddstudents = { "url" : "123", "item" : "erroruser" }
	def test_caaddstudents(self):
		print ("Test:Addstudents===============================")

		testuser = Students.query.filter_by(username = "test1").first()
		if testuser is None:
			testuser = Students(phonenumber = "12345678911", username = "test1", password = "123456")
		else:
			testuser.classroomlist = json.dumps([])
		db.session.add(testuser)
		db.session.commit()


		# 这是正确的结果
		response = self.app.post('/api/classroom/aaddstudents', data = json.dumps(self.data_aaddstudents, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不正确的结果
		response = self.app.post('/api/classroom/aaddstudents', data = json.dumps(self.dataerror_aaddstudents, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: no such student"}')


	def test_zdelete_classroom(self):
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')

		testuser = Students.query.filter_by(username = "test1").first()
		db.session.delete(testuser)
		db.session.commit()


	def test_classlist(self):
		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "adil", "password": "123456"}))
		self.assertEquals(type(json.loads(response.data.decode('utf8'))), list)

		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "error", "password": "123456"}))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')



	open_close_live_data = { "username" : "adil", "url" : "123456" }
	def test_open_close_live(self):
		print("test: open and close live")

		response = self.app.post('/api/classroom/openliving', data = json.dumps({ "username" : "adil", "url" : "123456" }))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")

		response = self.app.post('/api/classroom/closeliving', data = json.dumps({ "username" : "adil", "url" : "123456" }))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")


	def test_getstudents(self):
		print ("Test:Getstudents===============================")

		response = self.app.post('/api/classroom/getstudents', data = json.dumps({ "url" : "123" }))
		self.assertEquals(response.data.decode('utf8'), '["test1"]')


	def test_urlcheck(self):
		print ("Test:Urlcheck===============================")

		response = self.app.post('/api/classroom/urlcheck', data = json.dumps({ "username" : "test1", "url" : "123" }))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		response = self.app.post('/api/classroom/urlcheck', data = json.dumps({ "username" : "test2", "url" : "123" }))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error"}')

		response = self.app.post('/api/classroom/urlcheck', data = json.dumps({ "username" : "adil", "url" : "123456" }))
		self.assertEquals(response.data.decode('utf8'), '{"status": "password", "password": "123456"}')

		response = self.app.post('/api/classroom/urlcheck', data = json.dumps({ "username" : "adil", "url" : "654321" }))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error"}')


	def test_shutuplist(self):
		print ("Test:Shutuplist===============================")

		response = self.app.post('/api/classroom/shutuplist', data = json.dumps({ "url" : "123" }))
		self.assertEquals(response.data.decode('utf8'), '[]')
