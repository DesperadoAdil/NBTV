建立数据表操作：
create table classrooms(
id INT UNSIGNED NOT NULL PRIMARY KEY,
teacher VARCHAR(11) NOT NULL,
title VARCHAR(50) NOT NULL,
thumbnail VARCHAR(100) NOT NULL,
password VARCHAR(50) NOT NULL,
url VARCHAR(100) NOT NULL,
studentlist VARCHAR(1000) NOT NULL,
teacherlist VARCHAR(1000) NOT NULL,
audiencelist VARCHAR(1000) NOT NULL,
visible VARCHAR(5) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table teachers(
phonenumber VARCHAR(11) NOT NULL PRIMARY KEY,
password VARCHAR(50) NOT NULL,
classroomlist VARCHAR(1000) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table students(
phonenumber VARCHAR(11) NOT NULL PRIMARY KEY,
password VARCHAR(50) NOT NULL,
classroomlist VARCHAR(1000) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table resources(
id INT UNSIGNED NOT NULL PRIMARY KEY,
pdffilelist VARCHAR(1000) NOT NULL,
choicequestionlist INT UNSIGNED NOT NULL,
programquestionlist INT UNSIGNED NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table choicequestion(
id INT UNSIGNED NOT NULL PRIMARY KEY,
description VARCHAR(500) NOT NULL,
A VARCHAR(50) NOT NULL,
B VARCHAR(50) NOT NULL,
C VARCHAR(50) NOT NULL,
D VARCHAR(50) NOT NULL,
historysubmit VARCHAR(1000) NOT NULL,
answer VARCHAR(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table programquestion(
id INT UNSIGNED NOT NULL PRIMARY KEY,
description VARCHAR(500) NOT NULL,
language VARCHAR(20) NOT NULL,
historysubmit VARCHAR(1000) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

数据库结构：
	-----------------------------------						-----------------------------------
	|    teachers (		|						|    choicequestion (		|
	|    	phonenumber,<===|====					      ====	|=====>	id,		|
	|    	password,		|   ||   ||					      ||	|    	description,	|
        <==	|======	classroomlist	|   ||   ||					      ||	|    	A,B,C,D,		|
        ||	|    );			|   ||   ||					      ||	|    	historysubmit,	|
        ||	-----------------------------------   ||   ||					      ||	|    	answer		|
        ||				    ||   ||					      ||	|    );			|
        ||	-----------------------------------   ||   ||	----------------------------------------------     ||	-----------------------------------	
        ||	|    classrooms (		|   ||   ||	|    resources (			|     ||
        ===	|=====>	id,===========	|= ||=||==	|=====>	id,			|     ||
        ||	|    	teacher,========	|=>   ||	|    	pdffilelist,			|     ||
        ||	|    	title,		|        ||	|    	choicequestionlist,========	|===
        ||	|    	thumbnail,	|        ||	|    	programquestionlist=======	|===
        ||	|    	password,		|        ||	|    );				|     ||	-----------------------------------
        ||	|    	url,		|        ||	----------------------------------------------     ||	|    programquestion (	|
        ||	|    	studentlist,	|        ||					      ====	|=====> id,		|
        ||	|    	teacherlist,	|        ||						|    	description,	|
        ||	|    	audiencelist,=====	|===>						|    	language,		|
        ||	|    	visible		|        ||						|    	historysubmit	|
        ||	|    );			|        ||						|    );			|
        ||	-----------------------------------        ||						-----------------------------------
        ||				         ||
        ||	-----------------------------------        ||
        ||	|    students (		|        ||
        ||	|    	phonenumber,<===|====
        ||	|    	password,		|
        <==	|======	classroomlist	|
	|    );			|
	-----------------------------------