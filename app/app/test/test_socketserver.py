from app.test.BaseTestCase import BaseTestCase
from app.models import *
from app.classroom.Classroom import classroomManager
import unittest
import json

class SocketServerTest(BaseTestCase):
    def test_aon_connect(self):
        print ("Test:SocketIO_on_connect==============================================")

        self.socketio_client.emit("connect")

    def test_jon_disconnect(self):
        print ("Test:SocketIO_on_connect==============================================")

        self.socketio_client.emit("disconnect")

    def test_bon_join(self):
        print ("Test:SocketIO_on_join==============================================")

        self.socketio_client.emit('join', {'username': 'adil', 'url': '242544'})

    def test_csendMsg(self):
        print ("Test:SocketIO_sendMsg==============================================")

        self.socketio_client.emit('sendMsg', {'type': "broadcast", 'url': "242544"})

        self.socketio_client.emit('sendMsg', {'type': "whisper", 'fromUser': "adil", 'toUser': "stu1"})

        self.socketio_client.emit('sendMsg', {'type': "pdf", 'url': "242544"})

        self.socketio_client.emit('sendMsg', {'type': "page", 'url': "242544"})

        self.socketio_client.emit('sendMsg', {'type': "code", 'url': "242544"})

        self.socketio_client.emit('sendMsg', {'type': "select", 'url': "242544"})

        self.socketio_client.emit('sendMsg', {'type': "close", 'url': "242544"})

    def test_dlist(self):
        print ("Test:SocketIO_list==============================================")

        self.socketio_client.emit('list', {'username': 'adil', 'url': '242544'})

    def test_erefresh(self):
        print ("Test:SocketIO_refresh==============================================")

        self.socketio_client.emit('refresh', {'url': "242544"})

    def test_fcheck(self):
        print ("Test:SocketIO_check==============================================")

        self.socketio_client.emit('check', {'username': 'adil', 'url': '242544'})

    def test_iblacklist(self):
        print ("Test:SocketIO_blacklist==============================================")

        self.socketio_client.emit('blacklist', {'toUser': 'stu1', 'url': '242544'})

    def test_gshutup(self):
        print ("Test:SocketIO_shutup==============================================")

        self.socketio_client.emit('shutup', {'toUser': 'stu1', 'url': '242544'})

    def test_hnoShutUp(self):
        print ("Test:SocketIO_noShutUp==============================================")

        self.socketio_client.emit('noShutUp', {'username': 'stu1', 'url': '242544'})

    def test_kclear(self):
        print ("Test:SocketIO_clear==============================================")

        self.socketio_client.emit('clear')
