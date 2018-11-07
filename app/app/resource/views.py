from flask import *
from .MultiChoiceQuestion import multiChoiceManager
from .CodeQuestion import codeQuestionManager
from .PDFfile import pdfManager
from . import resource
from ..user.User import usermanager
import json

@resource.route('/add_multiple', methods = ['POST', 'GET'])
def addMultiChoice():
    data = request.get_data()
    print("add choice question")
    print(data)
    data = json.loads(data)
    ret = {}
    try:
        # data['optionList']是选择题选项的json字符串，还是一个list
        uniqueId = multiChoiceManager.insert(data['username'], data['statement'], data['optionList'], data['answer'])
        
        ret["status"] = "success"
        ret["uniqueId"] = uniqueId
    except Exception as err:
        print(err)
        ret["status"] = "error"
    return json.dumps(ret)

@resource.route('/delete_multiple', methods = ['POST', "GET"])
def deleteMultiple():
    print('delete choice question')
    data = resource.get_data()
    print(data)
    data = json.loads(data)
    ret = {}

    try:
        ret['status'] = multiChoiceManager.delete(data['uniqueId'])
    except Exception as err:
        print(err)
        ret['status'] = "error"
    return json.dumps(ret)


@resource.route('/update_multiple', methods = ['POST', 'GET'])
def updateMultiple():
    print('update choice question')
    data = resource.get_data()
    print(data)
    data = json.loads(data)
    ret = {}

    try:
        ret['status'] = multiChoiceManager.update(data['uniqueId'], data['statement'], data['optionList'], data['answer'])
    except Exception as err:
        print(err)
        ret['status'] = "error"
    return json.dumps(ret)


@resource.route('/getmultiples', methods = ['POST', 'GET'])
def getChoice():
    print('get a  choice question')
    data = resource.get_data()
    print(data)
    data = json.loads(data)
    ret = []

    try:
        username = data['username']
        teacher = usermanager.search("username", username, "teacher")
        data = teacher.choiceQue
        for item in data:
            ret.append({"statement": item.statement, "optionlist": json.loads(item.optionList), "answer": item.answer, "uniqueId": item.uniqueId})
        return json.dumps(ret)
    except Exception as err:
        print(err)
        return "error"


@resource.route('/add_code', methods = ['POST', 'GET'])
def addCode():
    print('add code question')
    ret = {}
    try:
        data = request.get_data()
        print(data)
        data = json.loads(data)

        uniqueId = codeQuestionManager.insert(data['username'], data['statement'], data['language'])
        ret["status"] = "success"
        ret["uniqueId"] = uniqueId
    except Exception as err:
        print(err)
        ret["status"] = "error"
    return json.dumps(ret)


@resource.route('/delete_code', methods = ['POST', 'GET'])
def delete_code():
    print('delete code question')
    data = request.get_data()
    print(data)
    data = json.loads(data)
    ret = {}
    ret['status'] = codeQuestionManager.delete(data['uniqueId'])
    return json.dumps(ret)

@resource.route('/update_code', methods = ['POST', 'GET'])
def update_code():
    print('update code question')
    data = request.get_data()
    print(data)
    data = json.loads(data)

    ret = {}
    ret['status'] = codeQuestionManager.update(data['uniqueId'], data['statement'], data['language'])
    return json.dumps(ret)


@resource.route('/getcodes', methods = ['POST', 'GET'])
def get_code():
    print('get a code')
    data = request.get_data()
    print(data)
    data = json.loads(data)
    ret = []

    try:
        username = data['username']
        teacher = usermanager.search("username", username, "teacher")
        data = teacher.codeQue
        for item in data:
            ret.append({"statement": item.statement, "language": item.language, "uniqueId": item.uniqueId})
        return json.dumps(ret)
    except Exception as err:
        print(err)
        return "error"

@resource.route('/add_pdf', methods = ['POST'])
def addPDF():
    print('add pdf file')
    ret = {}
    try:

        f = request.files.get['file']
        username = request.form['username']
        ret['status'] = pdfManager.insert(f, username)
        
    except Exception as err:
        print(err)
        ret['status'] = "error"
    return json.dumps(ret, ensure_ascii = False)

@resource.route('/delete_pdf', methods = ['POST'])
def delete_PDF():
    print('delet a pdf file')
    ret = {}
    try:
        data = request.get_data()
        print(data)
        data = json.loads(data)
        username = data['username']
        filename = data['title']
        ret['status'] = pdfManager.delete(username, filename)
    except Exception as err:
        print(err)
        ret['status'] = "error"
    return json.dumps(ret, ensure_ascii = False)



#Get_pdfs
@resource.route('/getpdfs', methods = ['POST'])
def get_pdfs():
    ret = []

    data = request.get_data()
    print (data)
    data = json.loads(data)

    username = data['username']
    # job = data['job']
    # url = data['url']
    # classroom = classroomManager.search(url)
    # if job == 'teacher' and classroom.teacher != username:
    #    print ("Get PDF Error: Wrong Teacher")
    #    ret['status'] 
    #    return json.dumps(ret)
    
    teacher = usermanager.search("username", username, "teacher")
    if teacher is None:
        # ret['status'] = "error"
        # return json.dumps(ret)
        return "error"


    data = teacher.pdfs
    for item in data:
        dic = {}
        dic['title'] = item.filename
        dic['url'] = "/pdf/" + username + "/" + item.filename
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



