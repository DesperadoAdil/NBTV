from ..MultiChoiceQuestion import multiChoiceManager

@resource.route('/api/resource/add_multiple', methods = ['POST', 'GET'])
def addMultiChoice():
	data = request.get_data()
	print("add choice question")
	print(data)
	data = json.loads(data)

	return multiChoiceManager.insert(data['statement'], data['optionList'], data['answer'])

