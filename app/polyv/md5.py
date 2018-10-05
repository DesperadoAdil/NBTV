import hashlib

def toMD5(stringValue):
	# 创建md5对象
	hl = hashlib.md5()
	# Tips
	# 此处必须声明encode
	# 否则报错为：hl.update(str)	Unicode-objects must be encoded before hashing
	hl.update(stringValue.encode(encoding='utf-8'))
	
	return hl.hexdigest().upper()
