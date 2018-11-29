from app.test.BaseTestCase import BaseTestCase
import json
from app.models import *
import unittest
from app.resource.MultiChoiceQuestion import multiChoiceManager

class Resource_Multi_Test(BaseTestCase):

	multi_data = {
			'statement': 'this is a test question in unit test',
			'optionList': ['option 1', 'option 2', 'option 3'],
			'answer': 'A',
			'username': 'adil'
		}

	def test_add_multi(self):
		
		response = self.app.post('/api/resource/add_multiple', data = json.dumps(self.multi_data))
		response_data = json.loads(response.data.decode('utf8')
		self.assertEquals(response_data['status'], "success"))

		try:
			multiChoiceManager.delete(response_data['uniqueId'])
		except:
			pass

	def test_delete_multi(self):
		uniqueId = multiChoiceManager.insert(self.multi_data['username'], self.multi_data['statement'], self.multi_data['optionList'], self.multi_data['answer'])

		response = self.app.post('/api/resource/delete_multiple', data = json.dumps({'uniqueId': uniqueId, 'username': username}))
		response_data = json.loads(response.data.decode('utf8'))
		self.assertEquals(response_data['status'], 'success')

	def test_update_multi(self):
		uniqueId = multiChoiceManager.insert(self.multi_data['username'], self.multi_data['statement'], self.multi_data['optionList'], self.multi_data['answer'])
		
		response = self.app.post('/api/resource/update_multiple', data = json.dumps({"uniqueId": uniqueId, "statement": self.multi_data['statement'], "optionList": self.multi_data['optionList'], "answer": "B"}))
		response_data = json.loads(response.data.decode('utf8'))
		self.assertEquals(response_data['status'], 'success')

		multiChoiceManager.delete(uniqueId)

	def test_get_multi(self):
		response = self.app.post('/api/resource/getmultiples', data = json.dumps({'username': 'adil'}))
		response_data = json.loads(response.data)

		self.assertEquals(type(response_data['multiAllList']), list)
		self.assertEquals(type(response_data['multiThisList']), list)

	def test_add_submit_view_del_multi_class(self):
		uniqueId = multiChoiceManager.insert(self.multi_data['username'], self.multi_data['statement'], self.multi_data['optionList'], self.multi_data['answer'])
		
		# add multi que to a class
		response = self.app.post('/api/resource/multi_addclass', data = json.dumps({'username': 'adil', 'url': '123456', 'uniqueId': uniqueId}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')

		# submit an answer for this question
		submit_data = {
			'answer': 'A', 
			'uniqueId': uniqueId,
			'username': 'stu1',
			'url': '123456'
		}
		response = self.app.post('/api/resource/multi_submit', data = json.dumps(submit_data))
		self.assertEquals(json.loads(response.data)['status'], 'success')

		# get submit record of this question
		response = self.app.post('/api/resource/multi_viewclass', data = json.dumps({'url': '123456', 'uniqueId': uniqueId}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')
		self.assertEquals(type(response_data['multiAnswerList']), list)

		# delete question from this classroom
		response = self.app.post('/api/resource/multi_delclass', data = json.dumps({'username': 'adil', 'url': '123456', 'uniqueId': uniqueId}))
		response_data = json.loads(response.data)
		self.assertEquals(response_data['status'], 'success')

		multiChoiceManager.delete(uniqueId)

