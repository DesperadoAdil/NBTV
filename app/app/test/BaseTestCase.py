import os
from app import app, socketio
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        self.socketio_client = socketio.test_client(app)
        print("test begin")

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(app.config['DATABASE'])
        print("test done")
