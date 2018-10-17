from .MultiChoiceQuestion import multiChoiceManager
from .CodeQuestion import codeQuestionManager
from .PDFfile import pdfManager

@resource.route('/add_multiple', methods = ['POST', 'GET'])
def addMultiChoice():
	data = request.get_data()
	print("add choice question")
	print(data)
	data = json.loads(data)

	uniqueId = multiChoiceManager.insert(data['statement'], data['optionList'], data['answer'])
	return "success"

@resource.route('/add_code', methods = ['POST', 'GET'])
def addCode():
	print('add code question')
	try:
		data = request.get_data()
		print(data)
		data = json.loads(data)

		uniqueId = codeQuestionManager.insert(data['statement'], data['language'])
		return "success"
	except Exception as err:
		print(err)
		return "error"

@resource.route('/add_pdf', methods = ['POST'])
def addPDF():
	print('add pdf file')
	try:
		f = request.files['file']
		username = request.form['username']
		pdfManager.insert(f, username)
		return "success"
	except:
		return "error"



