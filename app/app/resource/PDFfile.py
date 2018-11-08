from ..models import PDFFile
from werkzeug.utils import secure_filename
import os
from app import db
import shutil
import uuid

class PDF:
	def __init__(self):
		pass

	def insert(self, f, username):
		try:
			if not os.path.isdir('/mnt/NBTV/%s/' % username):
				os.mkdir('/mnt/NBTV/%s' % username)
			filename = '/mnt/NBTV/%s/%s' % (username, f.filename)
			f.save(filename)

			# uniqueId = str(uuid.uuid4())
			pdf = PDFFile(filePath = f.filename, owner = username, uniqueId = "%s/%s" % (username, f.filename))
			db.session.add(pdf)
			db.session.commit()

			return "success"
		except Exception as err:
			print('save pdf')
			print(err)
			return "error"

	def delete(self, username, fname):
		try:
			pdf = PDFFile.query.filter_by(owner = username, filename = fname).first()
			if pdf is None:
				return "error"
			db.session.delete(pdf)
			db.session.commit()
			shutil.move('/mnt/NBTV/%s/%s' % (username, fname), '/mnt/NBTV/garbage/%s' % (username + '_' + fname))

			return "success"
		except Exception as err:
			print(err)
			return "error"


pdfManager = PDF()
