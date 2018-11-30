from app.test.BaseTestCase import BaseTestCase
import json
from app.models import *
import unittest
from app.resource.PDFfile import pdfManager

class Resource_PDF_Test(BaseTestCase):

	def test_add_pdf(self):
		# 只能尝试错误添加
		response = self.app.post('/api/resource/add_pdf', data = {'file': 'gg', 'username': 'adil'})
		self.assertEquals(json.loads(response.data)['status'], 'error')

	def test_delete_pdf(self):
		data = {
			'username': 'adil',
			'pdf': {'title': 'xcj_gg', 'url': 'gggg'}
		}
		response = self.app.post('/api/resource/delete_pdf', data = json.dumps(data))
		self.assertEquals(json.loads(response.data)['status'], "error")


	def test_get_pdf(self):
		response = self.app.post('/api/resource/getpdfs', data = json.dumps({'username': 'adil', 'url': '123456'}))
		response_data = json.loads(response.data)

		self.assertEquals(type(response_data['pdfAllList']), list)
		self.assertEquals(type(response_data['pdfThisList']), list)

	def test_add_pdf_class(self):
		data = {
			'username': 'adil',
			'url': '123456',
			'pdf': {'title': 'gg', 'url': '/pdf/gggg'}
		}
		response = self.app.post('/api/resource/pdf_addclass', data = json.dumps(data))
		self.assertEquals(json.loads(response.data)['status'], 'error')

	def test_delete_pdf_class(self):
		data = {
			'url': '123456',
			'username': 'adil',
			'pdf': {'title': 'gg', 'url': '/pdf/gggg'}
		}
		response = self.app.post('/api/resource/pdf_delclass', data = json.dumps(data))
		self.assertEquals(json.loads(response.data)['status'], 'error')


