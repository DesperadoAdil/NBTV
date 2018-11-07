from app.test.BaseTestCase import BaseTestCase
import unittest
import json

class Classroom_stuTest(BaseTestCase):
    data_urlgetvid = { "url" : "242544" }
    dataerror_urlgetvid = { "url" : "242545" }

    def test_urlgetvid(self):
        print ("Test:Urlgetvid===============================")

        # 这是正确的结果
        response = self.app.post('/api/classroom_stu/urlgetvid', data = json.dumps(self.data_urlgetvid, ensure_ascii = False))
        self.assertEquals(response.data.decode('utf8'), '{"vid": "242544"}')

        # 这是不正确的结果
        response = self.app.post('/api/classroom_stu/urlgetvid', data = json.dumps(self.dataerror_urlgetvid, ensure_ascii = False))
        self.assertEquals(response.data.decode('utf8'), '{"vid": ""}')
