from app.test.BaseTestCase import BaseTestCase
from app.models import *
from app.classroom.Classroom import classroomManager
import unittest
import json

class ClasslistTest(BaseTestCase):
    def test_classlist(self):
        print ("Test:Classlist===============================")

        # 这是可以获取在线直播间列表的结果
        response = self.app.get('/api/list')
        self.assertIsNotNone(response.data.decode('utf8'))
