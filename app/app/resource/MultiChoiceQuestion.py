import json
from models import ChoiceQuestion


class MultiChoiceQuestion:
	def __init__(self):
		pass

	def insert(self, statement, optionList, answer):
		if statement == "":
			raise ValueError("your statement can not be null");
		if optionList == "":
			raise ValueError("your optionList can not be null");

		uniqueId = 
		que = ChoiceQuestion(uniqueId, statement = statement, optionList = json.dumps(optionList, ensure_ascii = False), answer = answer)
		db.session.add(que)
		db.commit()

		return uniqueId

	def update(self, uniqueId, statement, optionList, answer):
		try:
			que = ChoiceQuestion.query.filter(ChoiceQuestion.uniqueId == uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			que.statement = statement;
			que.optionList = optionList;
			que.answer = answer;
			db.session.add(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def delete(self, uniqueId):
		try:
			que = ChoiceQuestion.query.filter(ChoiceQuestion.uniqueId == uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			db.session.delete(que)
			db.session.commit()
			return "success"
		except:
			return "error"

	def getData(self, uniqueId):
		try:
			que = ChoiceQuestion.query.filter(ChoiceQuestion.uniqueId == uniqueId).first()
			if que is None:
				return "error:NoSuchQue"
			return {"statement": que.statement, "optionList": que.optionList, "answer": que.answer, "uniqueId": que.uniqueId}
		except:
			return "error"


multiChoiceManager = new MultiChoiceQuestion()
