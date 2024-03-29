# commit message符合规范
- 采用了Git Hook来检查每一次的commit message是否符合规范

## commit规范
commit message都要符合这一个规范：  
**Type #\d+：description**  

1. Type包括  
    1) **Feat**: 新功能（feature）  
    2) **Fix**: 修复bug  
    3) **Docs**: 文档  
    4) **Style**: 格式（不影响代码运行的变动）  
    5) **Refactor**: 重构  
    6) **Test**: 增加测试  
    7) **Chore**: 构建过程或辅助工具变动  

2. \#\d+: 为该commit关联的issue，每一个commit都应该关联至一个issue

## 增加脚本来控制commit message符合规范
将commit-msg文件拷贝到 .git/hooks/commit-msg即可

---
# API汇总
- ## 用户信息管理
   - ### 登录
      - **url:** */api/user/login*  
      - **description:** 检查username、password、job是否在数据库中  
      - **input:**  `{ username : '', password : '', job : 'student/teacher', loginway : 'username/phonenumber'}`
      - **output:** `{ status : 'success/error' }`
      - **frontend:** *Hanky*
      - **backend:** *Adil*

   - ### 注册
      - **url:** */api/user/register*  
      - **description:** 储存username、mobile、password、job到数据库，检查verification
      - **input:** `{ username : '', mobile : '', password : '', verification: '', job : 'student/teacher' }`
      - **output:** `{ status : 'success/error' }`
      - **frontend:** *Hanky*
      - **backend:** *Adil*

   - ### 手机验证码
      - **url:** */api/user/request_verification*
      - **description:** 接受post请求，获取input当中的mobile并且发送验证码
      - **input:** `{ mobile : '' }`
      - **output:** `{ status : 'success/error' }` *//验证码发送成功就返回success*
      - **frontend:** *Hanky*
      - **backend:** *Adil*

   - ### 修改密码
      - **url:** */api/user/change_password*
      - **description:** 修改用户密码
      - **input:** `{ status : 'login/logout', mobile : '', old_password : '', new_password : '', job : 'student/teacher' }`
      - **output:** `{ status : 'success/error' }` //修改成功就返回success
      - **frontend:** *Hanky*
      - **backend:** *Adil*

   - ### 修改手机号
      - **url:** */api/user/change_mobile*
      - **description:** 在此之前会进行两次验证码发送，验证码都通过后更改手机号
      - **input:** `{ status : 'login/logout', old_mobile : '', old_verification : '', new_mobile : '', new_verification : '', job : 'student/teacher' }`
      - **output:** `{ status : 'success/error' }` //修改成功就返回success
      - **frontend:** *Hanky*
      - **backend:** *Adil*

   - ### 获取用户观看的直播间列表
      - **url:** */api/user/mylist*
      - **description:** 获取用户观看的直播间教室列表
      - **input:** `{ username : '', job : 'student/teacher' }`
      - **output:** `[ {classrooms}, ... ]`
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

   - ### 用户删除自己观看的的直播间
      - **url:** */api/user/delmyclass*
      - **description:** 用户的删除自己观看的的直播间
      - **input:** `{ username : '', job : 'student/teacher', classroom : 'mylist中得到的直播间列表中的某一个直播间' }`
      - **output:** `{ status : 'success/error' }` //删除成功就返回success
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

- ## 资源管理

- #### 查看pdf文件列表

    - **url:** */api/resource/getpdfs*
    - **description:** 用户查看pdf文件，返回教师能用的和教室当中的列表 //返回两个pdf文件列表
    - **input:** `{ username : '', url: '' }`
    - **output:** `{ pdfAllList: [ '{ title : '', url : 'pdf文件路径(/pdf/username/filename.pdf)' }', ... ], pdfThisList: [...]}`
    - **frontend:** *yuxuan*
    - **backend:** *Adil*

- #### 从教师的教学资源中添加pdf到教室中

    - url: /api/resource/pdf_addclass
    - description: 为当前教室添加要使用的pdf课件
    - input: `{ username : '', url: '', pdf: {title: '', url: ''} }`
    - **output:** `{ status: "error"/"success"}`
    - **frontend:** *yuxuan*
    - **backend:** *Adil*

- #### 删除pdf文件

    - **url:** */api/resource/delete_pdf*
    - **description:** 用户删除pdf文件 //已有api，需要更改的是，不仅要从教师的文件列表中删除，还要从教室的文件列表中删除。返回两个更新后的列表
    - **input:** `{ username : '', url: '', pdf: {title: '', url: ''} }`
    - **output:** `{ status: "error"/"success" }`
    - **frontend:** *Yuxuan*
    - **backend:** *Adil*

- #### 从教室的使用资源中删除某个pdf文件

    - url: /api/resource/pdf_delclass
    - description: 从该教室的使用列表中删除，但不从教师的资源删除
    - input:** `{ username : '', url: '', pdf: {title: '', url: ''} }`
    - **output:** `{ status: "error"/"success" }`
    - frontend: yuxuan
    - backend: ???

- #### 查看选择题列表

    - **url:** */api/resource/getmutiples*
    - **description:** 用户查看选择题 // 输入用户名和当前url， 输出两个列表。一个是教师所有的选择题，一个是当前教室用的选择题。输出的每个选项都有一个uniqueId
    - **input:** `{username: '', url: ''}`
    - **output:** `{ multiAllList: [ '{ uniqueId: '', statement : '', optionList : '[ '答案列表', ... ]', answer : '一个数字' }', ... ], multiThisList: [...]}`
    - **frontend:** *Yuxuan*
    - **backend:** *Adil*

- #### 教师资源中添加选择题到教室中

    - url: /api/resource/multi_addclass
    - description: 添加已有的选择题到教室
    - input: `{username: '', url: '', uniqueId: ''}`
    - **output:** `{ status: "error"/"success" }`
    - **frontend:** *Yuxuan*
    - backend: ???

- #### 删除选择题

    - **url:** */api/resource/delete_mutiple*
    - **description:** 教师从全部资源中删除选择题
    - **input:** `{ username: '', url: '', uniqueId: ''}`
    - **output:** `{ status: "error"/"success" }` 
    - **frontend:** *Yuxuan*
    - **backend:** *???*

- #### 查看选择题答题情况

    - url: /api/resource/multi_viewclass
    - description：查看某个选择题目前所有的答题情况
    - **input:** `{ username: '', url: '', uniqueId: }`
    - **output:** `{ multiAnswerList: [ '{ student: '', answer : 'A / not answerered' }', ... ]}` // 返回该题目的学生答题列表
    - **frontend:** *Yuxuan*
    - backend

- #### 教室资源中删除选择题

    - url: /api/resource/multi_delclass
    - description：教室中删除，教师资源不变
    - **input:** `{ username: '', url: '', uniqueId: ''}`
    - **output:** `{ multiThisList: [...]}` // 返回更新后的列表
    - **frontend:** *Yuxuan*
    - backend

- #### 查看代码题列表 // 要更改

    - **url:** */api/resource/getcodes*
    - **description:** 用户查看代码题
    - **input:** `{ username : '', url: ''}`
    - **output:** `{ codeAllList: [ '{ uniqueId: '', statement : '', language : ''}', ... ], codeThisList: []}`  // 返回两个列表
    - **frontend:** *Yuxuan*
    - **backend:** *???*

- #### 教师资源中添加代码题到教室中

    - url：/api/resource/code_addclass
    - description：添加到教室列表中
    - **input:** `{ username : '', url: ''，uniqueId: ''}`
    - **output:** `{ status: "error"/"success" }`  // 返回教室中的列表
    - **frontend:** *Yuxuan*
    - backend

- #### 删除代码题

    - **url:** */api/resource/delete_code*
    - **description:** 教师从全部资源中删除代码题，同时删除教室中该资源
    - **input:** `{ username : '', url: ''， uniqueId: ''}`
    - **output:** `{ status: "error"/"success" }`  // 返回两个列表
    - **frontend:** *Yuxuan*
    - **backend:** *???*

- #### 教室中查看代码题提交结果

    - url: /api/resource/code_viewclass
    - description：查看代码题中所有学生的提交结果
    - **input:** `{ username : '', url: ''， uniqueId: '' }`
    - **output:** `{ codeAnswerList: [ '{ student: '', answer : '... / not answerered' }', ... ]}` // 返回该题目的学生答题列表
    - **frontend:** *Yuxuan*
    - backend

- #### 教室中删除代码题

    - url: /api/resource/code_delclass
    - description：教室中删除，教师资源不变
    - **input:** `{ username: '', url: '', uniqueId: ''}`
    - **output:** `{ status: "error"/"success" }` // 返回更新后的列表
    - **frontend:** *Yuxuan*
    - backend

   - ### pdf文件

      - ### 上传pdf文件
         - **url:** */api/resourse/add_pdf*
         - **description:** 上传pdf文件
         - **input:** ???
         - **output:** ???
         - **frontend:** *Yuxuan*
         - **backend:** *xcjthu*

      - ### 删除pdf文件
         - **url:** */api/resourse/delete_pdf*
         - **description:** 用户删除pdf文件
         - **input:** `{ username : '', title : '' }`
         - **output:** `{ status : 'success/error' }`
         - **frontend:** *Jamgun*
         - **backend:** *Adil*

     - ### 查看pdf文件列表
         - **url:** */api/resourse/getpdfs*
         - **description:** 用户查看pdf文件
         - **input:** `{ username : '' }`
         - **output:** `[ '{ title : '', url : 'pdf文件路径(/pdf/username/filename.pdf)' }', ... ]`
         - **frontend:** *Jamgun*
         - **backend:** *Adil*

   - ### 选择题
      - ### 添加选择题
         - **url:** */api/resourse/add_multiple*
         - **description:** 教师在教室中添加选择题
         - **input:** `{ statement : '', optionList : '[answer1, answer2,...]', answer : '一个数字', username : '' }`
         - **output:** `{ status : 'success/error', uniqueId : '' }`
         - **frontend:** *Yuxuan*
         - **backend:** *xcjthu*

      - ### 删除选择题
         - **url:** */api/resourse/delete_mutiple*
         - **description:** 教师在教室中删除选择题
         - **input:** `{ username : '', uniqueId : 'add_multiple中得到的uniqueId' }`
         - **output:** `{ status : 'success/error' }` //删除成功就返回success
         - **frontend:** *???*
         - **backend:** *???*

      - ### 修改选择题
         - **url:** */api/resourse/update_mutiple*
         - **description:** 教师在教室中修改选择题
         - **input:** `{ username : '', uniqueId : 'add_multiple中得到的uniqueId', statement : '', answer : '[{answer1,},{answer2,},...]', right : '一个数字' }`
         - **output:** `{ status : 'success/error' }` //修改成功就返回success
         - **frontend:** *???*
         - **backend:** *???*

      - ### 查看选择题
         - **url:** */api/resourse/getmutiples*
         - **description:** 用户查看选择题
         - **input:** `{ username : '' }`
         - **output:** `[ '{ statement : '', optionList : '[ '答案列表', ... ]', answer : '一个数字' }', ... ]`
         - **frontend:** *Jamgun*
         - **backend:** *Adil*

      - ### 查看选择题列表

         - **url:** */api/resourse/get_muti_list*
         - **description:** 用户获取该老师出过的选择题列表
         - **input:** `{ username : '' }`
         - **output:** `[ '{ statement : '', optionList : '[ '答案列表', ... ]', answer : '一个数字' }', ... ]`
         - **frontend:** *Jamgun*
         - **backend:** *Adil*

   - ### 代码题
      - ### 添加代码题
         - **url:** */api/resourse/add_code*
         - **description:** 教师在教室中添加代码题
         - **input:** `{ username : '', statement : '', language : '' }`
         - **output:** `{ status : 'success/error', uniqueId : '' }`
         - **frontend:** *Yuxuan*
         - **backend:** *xcjthu*

      - ### 删除代码题
         - **url:** */api/resourse/delete_code*
         - **description:** 教师在教室中删除代码题
         - **input:** `{ username : '', uniqueId : 'add_multiple中得到的uniqueId' }`
         - **output:** `{ status : 'success/error' }` //删除成功就返回success
         - **frontend:** *???*
         - **backend:** *???*

      - ### 修改代码题
         - **url:** */api/resourse/update_code*
         - **description:** 教师在教室中修改代码题
         - **input:** `{ username : '', uniqueId : 'add_multiple中得到的uniqueId', statement : '', language : '' }`
         - **output:** `{ status : 'success/error' }` //修改成功就返回success
         - **frontend:** *???*
         - **backend:** *???*

      - ### 查看代码题
         - **url:** */api/resourse/getcodes*
         - **description:** 用户查看代码题
         - **input:** `{ username : ''}`
         - **output:** `[ '{ statement : '', language : '' , students_work : [{username : '', code : ''}] }', ... ]`  //在每一项中新增学生错题情况的列表
         - **frontend:** *???*
         - **backend:** *???*


- ## 直播间管理
   - ### 在线直播间列表
      - **url:** */api/list*
      - **description:** 登录之后获取在线的直播间列表
      - **input:** `{ }`
      - **output:** `[ '{ classrooms }' ]`
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

   - ### 创建直播间
      - **url:** */api/classroom/add_class*
      - **description:** 教师登录后创建教室直播间
      - **input:** `{ username : '', password : '', title : '', thumbnail : '', class_password : '', url : '' ，img:''}`
      - **output:** `{ status : 'success/error' }` //创建成功就返回success
      - **frontend:** *Hanky*
      - **backend:** *xcjthu*

   - ### 删除直播间
      - **url:** */api/classroom/delete_class*
      - **description:** 教师删除直播间
      - **input:** `{ username : '', password : '', url : '' }`
      - **output:** `{ status : 'success/error' }` //删除成功就返回success
      - **frontend:** *Hanky*
      - **backend:** *xcjthu*

   - ### 修改直播间
      - **url:** */api/classroom/update_class*
      - **description:** 教师修改直播间的信息
      - **input:** `{ username : '', password : '', title : '', thumbnail : '', class_password : '', url : '', old_url : '' }`
      - **output:** `{ status : 'success/error' }` //修改成功就返回success
      - **frontend:** *Hanky*
      - **backend:** *xcjthu*

   - ### 教师的直播间教室列表
      - **url:** */api/classroom/user_living_list*
      - **description:** 获取教师的直播间教室列表
      - **input:** `{ username : '', password : '' }`
      - **output:** `[ {classrooms}, ... ]`
      - **frontend:** *Hanky*
      - **backend:** *xcjthu*

- ## 学生直播界面管理
   - ### 根据房间的url获取房间的vid
      - **url:** /api/classroom_stu/urlgetvid
      - **description:** 根据url返回房间的vid
      - **input:**  `{ url : '' }`
      - **output:** `{ vid : '' }`
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

- ## 老师直播界面管理
   - ### xlsx添加学生
      - **url:** /api/user/xlsxaddstudents
      - **description:** 前端给后端xlsx，后端返回学生列表
      - **input:**  `{ url : ''，item:''}` *注：item为xlsx文件*
      - **output:** `['zsh','xcj',...]` *注：返回的是成功加入的学生username*
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

   - ### 用户名添加学生
      - **url:** /api/user/aaddstudents
      - **description:** 前端给后端用户名，后端返回学生列表
      - **input:**  `{ url : ''，item:''}` *注：item为学生用户名*
      - **output:** `{ status : 'success/error' }`
      - **frontend:** *Jamgun*
      - **backend:** *Adil*

   - ### 获取某个学生的做题情况
      - **url:** /api/user/getstudentsti  
      - **description:** 返回某学生的做题情况
      - **input:**  `{ username : '', job : '', url : ''，item:''}`注：username为老师姓名，item为学生姓名
      - **output:** `[{ title : '',type : 'select/code', ans : '',standardans : '' },...]`
      - **frontend:** Jamgun
      - **backend:** ？

   - ### 通知后端：老师要展示某个PDF文件
      - **url:** /api/user/showpdfs  
      - **description:** 通知后端：老师要展示某个PDF文件，后端再通知学生端
      - **input:**  `{ username : '', job : '', url : ''，item:''}`注：username为老师姓名，item为PDF的title
      - **output:** 暂无
      - **frontend:** Jamgun
      - **backend:** ？****

   - ### 通知后端：老师要展示某选择题
      - **url:**/api/user/showselect
      - **description:** 通知后端：老师要展示某个选择题，后端再通知学生端
      - **input:**  `{ username : '', job : '', url : ''，item:''}`注：username为老师姓名，item为选择题的title
      - **output:** 暂无
      - **frontend:** Jamgun
      - **backend:** ？****

   - ### 通知后端：老师要退出教学资源
      - **url:**/api/user/closepdfsec
      - **description:** 通知后端：老师要退出教学资源，后端再通知学生端
      - **input:**  `{ username : '', job : '', url : ''}`注：username为老师姓名
      - **output:** 暂无
      - **frontend:** Jamgun
      - **backend:** ？****

   - ### 通知后端：老师要开播
      - **url:**/api/user/openliving
      - **description:** 通知后端：老师要开播，后端返回推流地址
      - **input:** `{ url : '' }`
      - **output:** `{ streamername : '', status : 'success/error' }`
      - **frontend:** *Jamgun*
      - **backend:** *xcjthu*

   - ### 通知后端：老师要关播
      - **url:**/api/user/closeliving
      - **description:** 通知后端：老师要关播，后端通知学生端
      - **input:**  `{ url : '' }`
      - **output:** `{ vid : '', status : 'success/error' }`
      - **frontend:** *Jamgun*
      - **backend:** *xcjthu*

---
##Socket通信
通信的消息都是下面的obj

  obj = {
    time: '', //小时:分钟
    msg: '',  //消息内容
    toUser: '', //目前为all，即群聊，之后加入私聊功能会用username
    fromUser: ''  //发消息的用户名
  }
### 加入聊天室
初始化socket，链接到url

  io.connect(io.connect(url, {'force new connection': true}) //此处需要后端给定url
链接后端服务器，会调用

  socket.on('open', 随意) //此处需要后端emit消息
用来判断是否成功连接聊天室，然后调用

  socket.emit('addUser', username)  //此处需要后端接收消息
给后端发送消息，用来将当前用户加入聊天室
###发送消息
​ socket.emit('sendMsg', obj)
###接收消息
​ socket.on('to' + username, obj)

# 数据库表结构
## NBTV
数据表|功能|
:---:|:---:
classrooms|存储教室信息
students|存储学生信息
teachers|存储教师信息
pdffile|存储pdf文件
choicequestion|存储选择题
codequestion|存储代码题
messages|存储短信验证码

## 几个中间表

数据表 | 描述 |
:---: | :--:|
classroom_choice | 教室与选择题资源的中间表
classroom_code | 教室与代码题的中间表
classroom_pdf | 教室与pdf文件的中间表

## 数据表结构
classrooms|detail
:---:|:---:
vid|保利威视推流vid
teacher|直播间教师username
title|直播间标题
thumbnail|直播间缩略图
mode|直播间隐私模式
password|直播间密码
url|直播间url
rtmpUrl|保利威视推流url
studentlist|直播间学生的username列表
teacherlist|直播间教师的username列表，这里教师相当于学生
audiencelist|直播间正在观看的观众username列表
visible|直播间知否可见
createtime|直播间创建日期
showtime|直播间开播时间
blacklist|直播间黑名单
shutuplist|禁言名单
choice|选择题（外键约束）
code|代码题（外键约束）
pdffile|pdf文件（外键约束）

students|detail
:---:|:---:
phonenumber|学生电话号码
username|学生用户名
password|学生密码
classroomlist|学生加入的直播间的url列表

teachers|detail
:---:|:---:
phonenumber|教师电话号码
username|教师用户名
password|教师密码
classroomlist|教师加入的直播间的url列表
classroom|教师创建的直播间的类对象列表
pdfs|老师上传的所有pdf文件
codeQue|老师上传的所有代码题
choiceQue|老师上传的所有选择题

pdffile|detail
:---:|:---:
uniqueId|pdf文件ID
owner|pdf文件所属的老师
filename|pdf文件的文件名


choicequestion|detail
:---:|:---:
uniqueId|选择题ID
statement|选择题题目
optionList|选择题选项列表
answer|选择题正确答案
submitRecord|选择题提交记录列表
owner|选择题所属的老师的username（外键约束）


codequestion|detail
:---:|:---:
uniqueId|代码题ID
statement|代码题题目
language|代码题规定语言
submitRecord|代码题提交记录列表
owner|代码题所属的老师（外键约束）

messages|detail
:---:|:---:
phonenumber|用户手机号
message|验证码
---
