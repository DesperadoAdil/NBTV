import json
from ..models import CodeQuestion
import uuid
from app import db

class CodeQuestionObj:
	def __init__(self):
		pass

	def insert(self, username, statement, language, ansCode):
		if statement == "" or language == "":
			return "error"
		uniqueId = str(uuid.uuid4())
		que = CodeQuestion(owner = username, uniqueId = uniqueId, statement = statement, language = language, submitRecord = "{}", ansCode = ansCode)
		db.session.add(que)
		db.session.commit()

		return uniqueId

	def update(self, uniqueId, statement, language, ansCode):
		try:
			que = CodeQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			que.statement = statement
			que.language = language
			que.ansCode = ansCode
			db.session.add(que)
			db.session.commit()

			return "success"
		except:
			return "error"

	def delete(self, uniqueId):
		try:
			que = CodeQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			db.session.delete(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def getData(self, uniqueId):
		try:
			que = CodeQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			return {"statement": que.statement, "uniqueId": que.uniqueId, "language": que.language, "submitRecord": que.submitRecord}
		except:
			return "error"

	def search(self, uniqueId):
		return CodeQuestion.query.filter_by(uniqueId = uniqueId).first()

	def submitAnswer(self, uniqueId, studentId, url, ans):
		try:
			que = CodeQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			record = json.loads(que.submitRecord)
			if not url in record:
				record[url] = {}
			record[url][studentId] = ans
			que.submitRecord = json.dumps(record, ensure_ascii = False)
			db.session.add(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def getSubmitAns(self, uniqueId, url):
		try:
			ret = []
			que = self.search(uniqueId)
			if que is None:
				return "error"
			record = json.loads(que.submitRecord)
			if url in record:
				for key in record[url]:
					ret.append({'student': key, 'answer': record[url][key]})
			return ret
		except:
			return "error"


codeQuestionManager = CodeQuestionObj()



