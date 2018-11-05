from app.test.BaseTestCase import BaseTestCase
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
		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/add_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')


	def test_bupdate_classroom(self):
		# 这是可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/update_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')


	def test_delete_classroom(self):
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.data, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "success"}')

		# 这是不可以正确插入的结果
		response = self.app.post('/api/classroom/delete_class', data = json.dumps(self.dataerror, ensure_ascii = False))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')


	def test_classlist(self):
		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "adil", "password": "123456"}))
		self.assertEquals(type(json.loads(response.data.decode('utf8'))), list)

		response = self.app.post('/api/classroom/user_living_list', data = json.dumps({"username": "error", "password": "123456"}))
		self.assertEquals(response.data.decode('utf8'), '{"status": "error:password wrong"}')



	open_close_live_data = {
		"username": "adil",
		"url": "123456"
	}
	def test_open_close_live(self):
		print("test: open and close live")

		response = self.app.post('/api/classroom/openliving', json.dumps(self.open_close_live_data))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")

		response = self.app.post('/api/classroom/closeliving', json.dumps(self.open_close_live_data))
		tmp = json.loads(response.data.decode('utf8'))
		self.assertEquals(tmp['status'], "success")




