from app.test.BaseTestCase import BaseTestCase
from app.models import *
from app.classroom.Classroom import classroomManager
import unittest
import json

class DeveloperTest(BaseTestCase):
    data_add_user = {}

    def test_add_user(self):
        print ("Test:Add_user===============================")

        # 这是可以插入用户的结果
        response = self.app.get('/developer/add_user')
        self.assertIsNotNone(response.data.decode('utf8'))


    def test_add_classroom(self):
        print ("Test:Add_classroom===============================")

        # 这是可以插入教室的结果
        response = self.app.get('/developer/add_classroom')
        self.assertIsNotNone(response.data.decode('utf8'))
