API汇总

1.
url:/api/user/login
description:检查username、password、job是否在数据库中
input:
{
	username	: '',
	password	: '',
	job			: 'student/teacher',
}

output:
{
	status		: 'success/error',
}

2.
url:/api/user/register
description:储存username、mobile、password、job到数据库，检查verification
input:
{
	username	: '',
	mobile		: '',
	password	: '',
	verification: '',		
	job			: 'student/teacher',
}
output:
{
	status		: 'success/error',
}

3.
url:/api/user/request_verification
description:接受post请求，获取input当中的mobile并且发送验证码
input:
{
	mobile		: '',
}
output:
{
	status		: 'success/error', //验证码发送成功就返回success
}


4.
url:/api/user/change_password
description:
input:
{
	status		: 'login/logout',
	mobile:		: '',
	old_password: '',
	new_password: '',
}
output:
{
	status		: 'success/error', //修改成功就返回success
}

5.
url:/api/user/change_mobile
description: 在此之前会进行两次验证码发送，验证码都通过后更改mobile
input:
{
	status		: 'login/logout',
	old_mobile	: '',
	old_verification: ''
	new_mobile	: '',
	new_verification: ''
}
output:
{
	status		: 'success/error', //修改成功就返回success
}

6.
url:/api/resourse/add_pdf
description:
input:
???
output:

7.
url:/api/resourse/add_mutiple
description:
input:
{
	number:''
	type:'mutiple'
	description:'',
	answer: [{answer1,},{answer2,},...]
	right: ''//一个数字
}
output:

8.
url:/api/resourse/delete_mutiple
description:
input:
{
	number:''
	type:'mutiple'
}
output:

9.
url:/api/resourse/update_mutiple
description:
input:
{
	number:'',
	type:'mutiple',
	description:'',
	answer: [{answer1,},{answer2,},...]
	right: ''//一个数字
}
output:

10.
url:/api/resourse/add_code
description:
input:
{
	number:'',
	type:'code'
	description:'',
	language:''
}
output:

11.
url:/api/resourse/delete_code
description:
input:
{
	number:''
	type:'code'
}
output:

12.
url:/api/resourse/update_code
description:
input:
{
	number:'',
	type:'code'
	description:'',
	language:''
}
output:

13.
url:/api/classroom/get_list
description:
input:
output:
{
	class_list:[{class1, [details_list]},{...}]
}

14.
url:/api/classroom/add_class
description:
input:
{
	title:
	img:
	password:
	teacher_info:
	{

	}
}
output:

15.
url:/api/classroom/update_class
description:
input:
{
	number:
	type:'classroom'
	title:
	img:
	password:
	teacher_info:
	{

	}
}
output:

16.
url:/api/classroom/add_student
description:
input:
{
	number:
	type:'classroom'
	student_list:[{student_info}]
	teacher_info:
	{

	}
}
output:

17.
url:/api/classroom/choose_resourse
description:
input:
{
	???
}
output:

