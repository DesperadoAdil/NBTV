from app.test.BaseTestCase import BaseTestCase
import unittest
import json

class ClassroomTest(BaseTestCase):

	data = {
			"username": "adil",
			"password": "123456",
			"title": "adilnb",
			"class_password": "121121",
			"thumbnail": "/static/image/test.jpg",
			"url": "123"
		}

	dataerror = {
		"username": "adil",
		"password": "1234",
		"title": "adilnb",
		"class_password": "121121",
		"thumbnail": "/static/image/test.jpg",
		"url": "123"
	}

	def test_add_classroom(self):
		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: no such teacher or classroom"}')


	def test_delete_classroom(self):
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: no such teacher or classroom"}')


	def test_updateclass(self):
		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: no such classroom"}')

	def test_classlist(self):
		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "adil", "password": "123456"}))
		self.assertEquals(type(json.loads(response.data.decode('utf8'))), list)

		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "error", "password": "123456"}))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error: no such classroom"}')
