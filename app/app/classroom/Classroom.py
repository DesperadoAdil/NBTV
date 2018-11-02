import json
from ..models import *


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
		ret['filelist'] = classroom.filelist
		ret['visible'] = classroom.visible
		ret['createtime'] = str(classroom.createtime)
		return ret

	def insert(self, vid, rtmpUrl, teacher, title, thumbnail, passwd, url):
		#在调用这个接口之前，需要先判断是否是本用户插入的，需要验证密码
		try:
			classroomTmp = Classrooms(vid = vid, teacher = teacher, title = title, thumbnail = thumbnail, password = passwd, rtmpUrl = rtmpUrl, url = url)
			db.session.add(classroomTmp)
			db.session.commit()
			return "success"
		except Exception as err:
			print(err)
			return "error"

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

	def update(self, title, thumbnail, newUrl, passwd, oldUrl):
		#在调用这个接口之前，需要先判断是否是本用户删除的，需要验证密码
		try:
			tmpClass = Classrooms.query.filter_by(url = oldUrl).first()
			if tmpClass is None:
				return "error:NoSuchClassroom"

			tmpClass.title = title
			tmpClass.thumbnail = thumbnail
			tmpClass.url = newUrl
			tmpClass.password = passwd
			db.session.add(tmpClass)
			db.session.commit()

			return "success"
		except Exception as err:
			print("update classrooms: ", err)
			return "error"

	def search(self, url):
		return Classrooms.query.filter_by(url = url).first()


classroomManager = ClassroomManager()
