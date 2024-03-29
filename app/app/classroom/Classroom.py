import json
from ..models import *
from datetime import datetime, timedelta
import os

class ClassroomManager:
	def __init__(self):
		pass

	def dict(self, classroom):
		ret = {}
		ret['vid'] = classroom.vid
		ret['teacher'] = classroom.teacher
		ret['title'] = classroom.title
		ret['thumbnail'] = classroom.thumbnail
		ret['mode'] = classroom.mode
		ret['password'] = classroom.password
		ret['url'] = classroom.url
		ret['rtmpUrl'] = classroom.rtmpUrl
		ret['studentlist'] = classroom.studentlist
		ret['teacherlist'] = classroom.teacherlist
		ret['visible'] = classroom.visible
		ret['createtime'] = str(classroom.createtime)
		ret['showtime'] = str(classroom.showtime)
		ret['blacklist'] = classroom.blacklist
		ret['shutuplist'] = classroom.shutuplist
		ret['status'] = classroom.status
		return ret

	def insert(self, vid, rtmpUrl, teacher, title, imgfile, passwd, url, mode):
		#在调用这个接口之前，需要先判断是否是本用户插入的，需要验证密码
		try:
			if not imgfile is None:
				if not os.path.exists("/mnt/NBTV_Img/%s" % teacher):
					os.mkdir("/mnt/NBTV_Img/%s" % teacher)
				imgpath = "/mnt/NBTV_Img/%s/%s.%s" % (teacher, vid, imgfile.filename.split('.')[-1])
				imgfile.save(imgpath)
				imgUrl = '/img_class/%s/%s.%s' % (teacher, vid, imgfile.filename.split('.')[-1])
			else:
				imgUrl = '/static/image/test.jpg'

			classroomTmp = Classrooms(vid = vid, teacher = teacher, title = title, thumbnail = imgUrl, password = passwd, rtmpUrl = rtmpUrl, url = url, mode = mode, createtime = datetime.now() + timedelta(hours=8), showtime = datetime.now() + timedelta(hours=8))

			db.session.add(classroomTmp)
			db.session.commit()
			return "success"
		except Exception as err:
			print(err)
			return "error:该url已被占用"

	def delete(self, url):
		#在调用这个接口之前，需要先判断是否是本用户删除的，需要验证密码
		try:
			tmpClass = Classrooms.query.filter_by(url = url).first()
			if tmpClass is None:
				return "error:NoSuchClassroom"
			db.session.delete(tmpClass)
			db.session.commit()
			return "success"
		except Exception as err:
			print("delete classroom: ", err)
			return "error"

	def update(self, title, imgfile, newUrl, passwd, oldUrl):
		#在调用这个接口之前，需要先判断是否是本用户删除的，需要验证密码
		try:
			tmpClass = Classrooms.query.filter_by(url = oldUrl).first()
			if tmpClass is None:
				return "error:NoSuchClassroom"

			if not imgfile is None:
				imgpath = "/mnt/NBTV_Img/%s/%s.%s" % (tmpClass.teacher, tmpClass.vid, imgfile.filename.split('.')[-1])
				imgfile.save(imgpath)

			tmpClass.title = title
			# tmpClass.thumbnail = thumbnail
			tmpClass.url = newUrl
			tmpClass.password = passwd
			db.session.add(tmpClass)
			db.session.commit()

			return "success"
		except Exception as err:
			print("update classrooms: ", err)
			return "error: url已经被占用了"

	def updateShowTime(self, url, status):
		try:
			tmpClass = Classrooms.query.filter_by(url = url).first()
			if tmpClass is None:
				return "error: no such classroom"

			if status == "open":
				tmpClass.showtime = datetime.now() + timedelta(hours=8)
				tmpClass.status = json.dumps({'type': "openliving"})
			elif status == "close":
				tmpClass.status = json.dumps({'type': "closeliving"})
			else:
				return "error: unknown error"
			db.session.add(tmpClass)
			db.session.commit()
			return "success"
		except Exception as err:
			print("updateShowTime: ", err)
			return "error"


	def search(self, url):
		return Classrooms.query.filter_by(url = url).first()


classroomManager = ClassroomManager()
