from .MultiChoiceQuestion import multiChoiceManager
from .CodeQuestion import codeQuestionManager
from .PDFfile import pdfManager
from . import resource
import json

@resource.route('/add_multiple', methods = ['POST', 'GET'])
def addMultiChoice():
    data = request.get_data()
    print("add choice question")
    print(data)
    data = json.loads(data)
    ret = {}
    try:
        uniqueId = multiChoiceManager.insert(data['statement'], data['optionList'], data['answer'])
        ret["status"] = "success"
        ret["uniqueId"] = uniqueId
    except Exception as err:
        print(err)
        ret["status"] = "error"
    return json.dumps(ret)

@resource.route('/add_code', methods = ['POST', 'GET'])
def addCode():
    print('add code question')
    ret = {}
    try:
        data = request.get_data()
        print(data)
        data = json.loads(data)

        uniqueId = codeQuestionManager.insert(data['statement'], data['language'])
        ret["status"] = "success"
        ret["uniqueId"] = uniqueId
    except Exception as err:
        print(err)
        ret["status"] = "error"
    return json.dumps(ret)

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


#Get_pdfs
@resource.route('/getpdfs', methods = ['POST'])
def get_pdfs():
    ret = []

    data = request.get_data()
    print (data)
    data = json.loads(data)

    username = data['username']
    job = data['job']
    url = data['url']
    classroom = classroomManager.search(url)
    if job == 'teacher' and classroom.teacher != username:
        print ("Get PDF Error: Wrong Teacher")
        return ret

    data = json.loads(classroom.filelist)
    for item in data:
        dic = {}
        dic['title'] = item
        dic['url'] = "/pdf/" + username + "/" + item
        ret.append(dic)

    print (json.dumps(ret))
    return json.dumps(ret)


#Get_selects
@resource.route('/getselects', methods = ['POST'])
def get_selects():
    ret = []

    data = request.get_data()
    print (data)
    data = json.loads(data)

    username = data['username']
    job = data['job']
    url = data['url']
    classroom = classroomManager.search(url)
    if job == 'teacher' and classroom.teacher != username:
        print ("Get Selects Error: Wrong Teacher")
        return ret

    for item in classroom.choicequestion:
        dic = {}
        dic['title'] = item.statement
        dic['ans'] = item.optionList
        dic['answer'] = item.answer
        ret.append(dic)

    print (json.dumps(ret))
    return json.dumps(ret)
