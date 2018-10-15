from ..models import PDFFile
from werkzeug.utils import secure_filename
import os
import shutil

class PDF:
	def __init__(self):
		pass

	def insert(self, f, username):
		try:
			if not os.path.isdir('/mnt/NBTV/%s/' % username):
				os.mkdir('/mnt/NBTV/%s' % username)
			filename = '/mnt/NBTV/%s/%s' % (username, f.filename)
			f.save(filename)
			return "success"
		except Exception as err:
			print('save pdf')
			print(err)
			return "error"

	def delete(self, fname, username):
		try:
			shutil.move('/mnt/NBTV/%s/%s' % (username, fname), '/mnt/NBTV/garbage/%s' % (username + '_' + fname))
			return "success"
		except Exception as err:
			return "error"


pdfManager = PDF()
