# -*- coding: utf-8 -*-
import hashlib
import sys

class CreateMD5:
	def __init__(self):
		print "CreateMD5 creat!"

	def md5sumSmallFile(self, filename, path):
		fullName = path + "/" + filename
		try :
			fd = open(fullName, "r")
		except :
			print "open file failure..."
		fcont = fd.read()
		fmd5 = hashlib.md5(fcont)
		return fmd5


if __name__ == '__main__': 
	cfmd5 = CreateMD5()
	print cfmd5.md5sumSmallFile('config.yaml', '/root/emsys/syn_files_test').hexdigest()

