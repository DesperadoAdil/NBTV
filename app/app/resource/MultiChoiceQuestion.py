import json
from ..models import ChoiceQuestion
import uuid
from app import db

class MultiChoiceQuestion:
	def __init__(self):
		pass

	def insert(self, username, statement, optionList, answer):
		if statement == "":
			raise ValueError("your statement can not be null");
		if optionList == "":
			raise ValueError("your optionList can not be null");

		uniqueId = str(uuid.uuid4())

		que = ChoiceQuestion(owner = username, uniqueId = uniqueId, statement = statement, optionList = json.dumps(optionList, ensure_ascii = False), answer = answer, submitRecord = "{}")
		db.session.add(que)
		db.session.commit()


		return uniqueId

	def update(self, uniqueId, statement, optionList, answer):
		try:
			que = ChoiceQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			que.statement = statement;
			que.optionList = json.dumps(optionList, ensure_ascii = False);
			que.answer = answer;
			db.session.add(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def delete(self, uniqueId):
		try:
			que = ChoiceQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			db.session.delete(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def getData(self, uniqueId):
		try:
			que = ChoiceQuestion.query.filter_by(uniqueId = uniqueId).first()
			if que is None:
				return "error:NoSuchQue"

			return {"statement": que.statement, "optionList": que.optionList, "answer": que.answer, "uniqueId": que.uniqueId, "submitRecord": que.submitRecord}
		except:
			return "error"

	def search(self, uniqueId):
		return ChoiceQuestion.query.filter_by(uniqueId = uniqueId).first()

	def submitAnswer(self, uniqueId, studentId, url, ans):
		try:
			que = ChoiceQuestion.query.filter_by(uniqueId = uniqueId).first()
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
		except Exception as err:
			print(err)
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


multiChoiceManager = MultiChoiceQuestion()

