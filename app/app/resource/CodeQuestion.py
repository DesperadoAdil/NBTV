import json
from ..models import CodeQuestion

class CodeQuestionObj:
	def __init__(self):
		pass

	def insert(self, statement, language):
		if statement == "" or language == "":
			return "error"
		uniqueId = 
		que = CodeQuestion(uniqueId = uniqueId, statement = statement, language = language, submitRecord = "[]")
		db.session.add(que)
		db.session.commit()

		return uniqueId

	def update(self, uniqueId, statement, language):
		try:
			que = CodeQuestion.query.filter(CodeQuestion.uniqueId == uniqueId)
			if que is None:
				return "error:NoSuchQue"
			que.statement = statement
			que.language = language
			db.session.add(que)
			db.session.commit()

			return "success"
		except:
			return "error"

	def delete(self, uniqueId):
		try:
			que = CodeQuestion.query.filter(CodeQuestion.uniqueId == uniqueId)
			if que is None:
				return "error:NoSuchQue"
			db.session.delete(que)
			db.commit()
			return "success"
		except:
			return "error"

	def getData(self, uniqueId):
		try:
			que = CodeQuestion.query.filter(CodeQuestion.uniqueId == uniqueId)
			if que is None:
				return "error:NoSuchQue"
			return {"statement": que.statement, "uniqueId": que.uniqueId, "language": que.language, "submitRecord": que.submitRecord}
		except:
			return "error"

	def submitAnswer(self, uniqueId, studentId, ans):
		try:
			que = CodeQuestion.query.filter(CodeQuestion.uniqueId == uniqueId)
			if que is None:
				return "error:NoSuchQue"
			record = json.loads(que.submitRecord)
			record.append([studentId, ans])
			que.submitRecord = json.dumps(record, ensure_ascii = False)
			db.session.add(que)
			db.session.commit()
			return "success"
		except:
			return "error"


codeQuestionManager = CodeQuestionObj()



