from app.test.BaseTestCase import BaseTestCase
import json
from app.models import *
import unittest
from app.resource.CodeQuestion import codeQuestionManager

class Resource_Code_Test(BaseTestCase):
	code_data = {
		'username': 'adil',
		'statement': '请计算a+b；\n输入：整数 a，整数 b；\n输出 a+b',
		'language': 'python',
		'example': 'print(a+b)'
	}

	def test_add_code(self):
		response = self.app.post('/api/resource/add_code', data = json.dumps(self.code_data))
		response_data = json.loads(response.data.decode('utf8'))
		self.assertEquals(response_data['status'], "success")

		codeQuestionManager.delete(response_data['uniqueId'])

	def test_delete_code(self):
		uniqueId = codeQuestionManager.insert(self.code_data['username'], self.code_data['statement'], self.code_data['language'], self.code_data['example'])

		response = self.app.post('/api/resource/delete_code', data = json.dumps({'uniqueId': uniqueId}))
		self.assertEquals(json.loads(response.data)['status'], 'success')

	def test_update_code(self):
		uniqueId = codeQuestionManager.insert(self.code_data['username'], self.code_data['statement'], self.code_data['language'], self.code_data['example'])
		
		self.code_data['uniqueId'] = uniqueId
		response = self.app.post('/api/resource/update_code', data = json.dumps(self.code_data))		
		self.assertEquals(json.loads(response.data)['status'], 'success')

		codeQuestionManager.delete(uniqueId)

	def test_get_codes(self):
		response = self.app.post('/api/resource/getcodes', data = json.dumps({"username": "adil", "url": "123456"}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')
		self.assertEquals(type(response_data['codeAllList']), list)
		self.assertEquals(type(response_data['codeThisList']), list)

	def test_add_submit_view_delete_code_class(self):
		uniqueId = codeQuestionManager.insert(self.code_data['username'], self.code_data['statement'], self.code_data['language'], self.code_data['example'])
		
		# add code to a class
		response = self.app.post('/api/resource/code_addclass', data = json.dumps({"username": "adil", "url": "123456", "uniqueId": uniqueId}))
		self.assertEquals(json.loads(response.data)['status'], 'success')

		# submit a code to a class
		submit_data = {
			'answer': 'printf(adil nb!)', 
			'uniqueId': uniqueId,
			'username': 'stu1',
			'url': '123456'
		}
		response = self.app.post('/api/resource/code_submit', data = json.dumps(submit_data))
		self.assertEquals(json.loads(response.data)['status'], 'success')

		# view submit record
		response = self.app.post('/api/resource/code_viewclass', data = json.dumps({"username": "adil", "url": "123456", "uniqueId": uniqueId}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')
		self.assertEquals(type(response_data['codeAnswerList']), list)

		# delete code from a class
		response = self.app.post('/api/resource/code_delclass', data = json.dumps({"username": "adil", "url": "123456", "uniqueId": uniqueId}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')

		codeQuestionManager.delete(uniqueId)