
'''const for login'''
Database = "NBTV"
passwd = "root12345"
User = "root"
IP = "localhost"


'''table name'''
ChoiceQueTable = "choicequestion"
ClassroomTable = "classrooms"
ProgramQueTable = "programquestion"
ResourceTable = "resources"
StudentTable = "students"
TeacherTable = "teachers"


'''the column name of each table'''
ChoiceQueTableCol = ["id", "description", "A", "B", "C", "D", "historysubmit", "answer"]
ClassroomTableCol = ["id", "teacher", "title", "thumbnail", "password", "url", "studentlist", "teacherlist", "audiencelist", "visible"]
ProgramQueTableCol = ["id", "description", "language", "historysubmit"]
ResourceCol = ["id", "pdffilelist", "choicequestionlist", "programquestionlist"]
StudentCol = ["phonenumber", "password", "classroomlist"]
TeacherCol = ["phonenumber", "password", "classroomlist"]


'''table name -> columns'''
GetCols = {
	ChoiceQueTable: ChoiceQueTableCol, 
	ClassroomTable: ClassroomTableCol, 
	ProgramQueTable: ProgramQueTableCol, 
	ResourceTable: ResourceCol, 
	TeacherTable: TeacherCol,
	StudentTable: StudentCol
	}
def getColNames(tableName):
	return GetCols[tableName]


