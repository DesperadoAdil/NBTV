import MySQLdb
from db import const
import json


operator = MySQLdb.connect(const.IP, const.User, const.passwd, const.Database, charset = "utf8")
cursor = operator.cursor()


def toStr(v):
	if (type(v) == str):
		return '"%s"' % v
	else:
		return str(v)

def insertData(tableName, value):
	'''type(value) == dict'''
	'''
		insert failed if return false
		insert success if return true
	'''
	keyname = ''
	valuelist = ''
	for key in value.keys():
		keyname += key + ','
		valuelist += toStr(value[key])
	
	sql = "insert into %s(%s) values(%s)" % (tableName, keyname[:-1], valuelist[:-1])


	num = cursor.excute(sql)
	operator.commit()

	return num > 0


def updataData(tableName, priKey, value):
	setStmt = ""
	for key in value.keys():
		setStmt += '%s = %s' % (key, toStr(value[key]))

	keyname = priKey.keys()[0]
	sql = "update %s set %s where %s = %s" % (tableName, setStmt[:-1], keyname, priKey[keyname])
	num = cursor.excute(sql)
	operator.commit()

	return num > 0


def fetchOneData(tableName, priKey):
	keyname = priKey.keys()[0]

	sql = "select * from %s where %s = %s" % (tableName, keyname, priKey[keyname])

	cursor.excute(sql)

	result = cursor.fetchone()
	if result is None:
		return None
	else:
		ans = {}
		colName = const.getColNames(tableName)
		for i in range(len(colName)):
			ans[colName[i]] = result[i]

		return ans

def deleteOneData(tableName, priKey):
	keyname = priKey.keys()[0]

	sql = "delete from %s where %s = %s" % (tableName, keyname, priKey[keyname])

	cursor.excute(sql)
	operator.commit()


