from flask import *
from .MultiChoiceQuestion import multiChoiceManager
from .CodeQuestion import codeQuestionManager
from .PDFfile import pdfManager
from . import resource
from ..user.User import usermanager
from ..classroom.Classroom import classroomManager
import json
from app import db

@resource.route('/add_multiple', methods = ['POST', 'GET'])
def addMultiChoice():
    data = request.get_data()
    print("add choice question")
    #print(data)
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
    data = request.get_data()
    #print(data)
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
    data = request.get_data()
    #print(data)
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
    print('get a choice question')
    data = request.get_data()
    data = json.loads(data)

    ret = {'multiAllList': [], 'multiThisList': []}

    try:
        username = data['username']
        teacher = usermanager.search("username", username, "teacher")
        
        for item in teacher.choiceQue:
            ret['multiAllList'].append({"statement": item.statement, "optionlist": json.loads(item.optionList), "answer": item.answer, "uniqueId": item.uniqueId})
        clr = classroomManager.search(data['url'])
        for item in clr.choice:
            ret['multiThisList'].append({"statement": item.statement, "optionlist": json.loads(item.optionList), "answer": item.answer, "uniqueId": item.uniqueId})
        # return json.dumps(ret)
        ret['status'] = "success"
    except Exception as err:
        print(err)
        ret['status'] = "error"

    return json.dumps(ret)

@resource.route('/multi_addclass', methods = ['POST', 'GET'])
def add_choice_class():
    print('add choice to class')
    data = request.get_data()
    data = json.loads(data)
    
    ret = {}

    choice_tmp = multiChoiceManager.search(data['uniqueId'])
    if choice_tmp is None or choice_tmp.owner != data['username']:
        print('gg: choice_tmp is None or choice_tmp.owner != username')
        ret['status'] = 'error'
        return json.dumps(ret)

    clr = classroomManager.search(data['url'])
    if clr is None or clr.teacher != data['username']:
        print('gg : something go wrong with classroom and teacher')
        ret['status'] = 'error'
        return json.dumps(ret)

    clr.choice.append(choice_tmp)
    db.session.add(clr)
    db.session.commit()

    ret['status'] = 'success'
    return json.dumps(ret)

@resource.route('/api/resource/multi_viewclass', methods = ['POST', 'GET'])
def view_choice_class():
    print('view choice class')
    data = json.loads(request.get_data())

    ret = {}
    choice_tmp = multiChoiceManager.search(data['uniqueId'])
    if choice_tmp is None:
        print('gg: choice_tmp is None')
        ret['status'] = 'error'
        return json.dumps(ret)

    ret['multiAnswerList'] = json.loads(choice_tmp.submitRecord)
    return json.dumps(ret)


@resource.route('/add_code', methods = ['POST', 'GET'])
def addCode():
    print('add code question')
    ret = {}
    try:
        data = request.get_data()
        #print(data)
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
    #print(data)
    data = json.loads(data)
    ret = {}
    ret['status'] = codeQuestionManager.delete(data['uniqueId'])
    return json.dumps(ret)

@resource.route('/update_code', methods = ['POST', 'GET'])
def update_code():
    print('update code question')
    data = request.get_data()
    #print(data)
    data = json.loads(data)

    ret = {}
    ret['status'] = codeQuestionManager.update(data['uniqueId'], data['statement'], data['language'])
    return json.dumps(ret)

@resource.route('/code_addclass', methods = ['POST', 'GET'])
def add_code_class():
    print('add code to class')
    data = request.get_data()
    data = json.loads(data)

    ret = {}

    clr = classroomManager.search(data['url'])
    if clr is None or clr.teacher != data['username']:
        print('gg: clr is None or clr.teacher != username')
        ret['status'] = 'error'
        return json.dumps(ret)

    code_tmp = codeQuestionManager.search(data['uniqueId'])
    if code_tmp is None or code_tmp.owner != data['username']:
        print('gg: code is wrong')
        ret['status'] = 'error'
        return json.dumps(ret)

    clr.code.append(code_tmp)
    db.session.add(clr)
    db.session.commit()

    ret['status'] = 'success'
    return json.dumps(ret)

@resource.route('/code_viewclass', methods = ['POST', 'GET'])
def view_code_class():
    print('view code class')
    data = json.loads(request.get_data())
    
    ret = {}
    
    code_tmp = codeQuestionManager.search(data['uniqueId'])
    if code_tmp is None or code_tmp.owner != data['username']:
        print('gg: code is wrong')
        ret['status'] = 'error'
        return json.dumps(ret)

    ret['codeAnswerList'] = json.loads(code_tmp.submitRecord)
    ret['status'] = 'success'
    return json.dumps(ret)

@resource.route('/code_delclass', methods = ['POST', 'GET'])
def code_delete_class():
    print('view code class')
    data = json.loads(request.get_data())
    ret = {}

    clr = classroomManager.search(data['url'])
    if clr is None or clr.teacher != data['username']:
        print('gg: clr is None or clr.teacher != username')
        ret['status'] = 'error'
        return json.dumps(ret)
    code_tmp = codeQuestionManager.search(data['uniqueId'])
    if code_tmp is None or code_tmp.owner != data['username']:
        print('gg: code is wrong')
        ret['status'] = 'error'
        return json.dumps(ret)
    clr.code.remove(code_tmp)
    db.session.add(clr)
    db.session.commit()

    ret['status'] = 'success'
    return json.dumps(ret)


@resource.route('/getcodes', methods = ['POST', 'GET'])
def get_code():
    print('get a code')
    data = request.get_data()
    #print(data)
    data = json.loads(data)
    ret = {'codeAllList': [], 'codeThisList': []}

    try:
        username = data['username']
        teacher = usermanager.search("username", username, "teacher")
        
        for item in teacher.codeQue:
            ret['codeAllList'].append({"statement": item.statement, "language": item.language, "uniqueId": item.uniqueId})
        clr = classroomManager.search(data['url'])
        for item in clr.code:
            ret['codeThisList'].append({"statement": item.statement, "language": item.language, "uniqueId": item.uniqueId})
        ret['status'] = 'success'
    except Exception as err:
        print(err)
        ret['status'] = 'error'
    return json.dumps(ret)

@resource.route('/add_pdf', methods = ['POST'])
def add_PDF():
    print('add pdf file')
    ret = {}
    try:
        f = request.files.get('file')
        username = request.form.to_dict()['username']
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
        #print(data)
        data = json.loads(data)
        username = data['username']
        filename = data['pdf']['title']
        ret['status'] = pdfManager.delete(username, filename)
    except Exception as err:
        print(err)
        ret['status'] = "error"
    return json.dumps(ret, ensure_ascii = False)


@resource.route('/pdf_delclass', methods = ['POST', 'GET'])
def delete_class_PDF():
    print('delete a pdf file from class')
    data = request.get_data()
    data = json.loads(data)

    ret = {}

    clr = classroomManager.search(data['url'])
    if clr is None or clr.teacher != data['username']:
        print('gg: clr is None or clr.teacher != username')
        ret['status'] = 'error'
        return json.dumps(ret)

    pdf_tmp = pdfManager.search(data['username'], data['pdf']['title'])
    if pdf_tmp is None:
        print('gg: pdf_tmp is None')
    clr.pdffile.remove(pdf_tmp)

    ret['status'] = 'success'
    return json.dumps(ret)
    

#Get_pdfs
@resource.route('/getpdfs', methods = ['POST'])
def get_pdfs():
    print('get pdf list')

    ret = {'pdfAllList': [], 'pdfThisList': []}

    data = request.get_data()
    # print (data)
    data = json.loads(data)

    username = data['username']

    teacher = usermanager.search("username", username, "teacher")
    if teacher is None:
        ret['status'] = "error"
        return json.dumps(ret)
        # return "error"

    for item in teacher.pdfs:
        ret['pdfAllList'].append({
            'title': item.filename,
            'url': "/pdf/%s/%s" % (username, item.filename)
            })

    url = data['url']
    clr = classroomManager.search(url)
    if clr is None:
        ret['status'] = "error"
        return json.dumps(ret)
    for item in clr.pdfs:
        ret['pdfThisList'].append({
            'title': item.filename,
            'url': "/pdf/%s/%s" % (username, item.filename)
            })

    ret['status'] = 'success'
    print (json.dumps(ret))
    return json.dumps(ret)

@resource.route('/pdf_addclass', methods = ['POST', 'GET'])
def add_pdf_class():
    print('add pdf to class')
    data = request.get_data()
    data = json.loads(data)

    ret = {}

    username = data['username']
    url = data['url']

    clr = classroomManager.search(url)
    if clr is None or clr.teacher != username:
        ret['status'] = 'error'
        print('the classroom do not belong to the teacher or no such classroom')
        return json.dumps(ret)

    pdffile = pdfManager.search(data['pdf']['url'][5:])
    if pdffile is None:
        ret['status'] = 'error'
        print('gg: no such pdffile')
        return json.dumps(ret)

    clr.pdffile.append(pdffile)
    db.session.add(clr)
    db.session.commit()

    ret['status'] = 'success'
    return json.dumps(ret)

