# -*- coding: utf-8 -*-

import os
import time, stat, copy
import pickle
import creatMD5

class ChechFiles:

	def __init__(self, path):
		self.path = path
		print self.path		
		self.fileNames = []

		self.fileAtr = {} 	#内存中的文件信息
		self.storedFileAtr = {} #存储的文件信息
		self.updateFileAtr = {} #需要升级的文件信息

		self.cfmd5 = creatMD5.CreateMD5() #md5生成模块

		self.readFileFromPath() #读取当前目标文件夹下的 文件的名字 存到self.fileNames
		#self.readFileAtr()
		self.getStoredFileAtr() #读取老的文件信息
		self.readFileAtr(self.fileAtr) #读取当前目标文件信息
		print "get stored info",
		print self.storedFileAtr
		self.ServerInitFileDateCheck()

		
	def readFileFromPath(self):
		
		for name in os.listdir(self.path):
			#print name
			if os.path.isfile(self.path + "\\" + name) :
				self.fileNames.append(name)

	def readFileAtr(self, atr):

		for file in self.fileNames:
			st = os.stat(self.path + "\\" + file)
			atr[file] = []
			atr[file].append(oct(stat.S_IMODE(st[stat.ST_MODE])))
			atr[file].append(time.ctime(st[stat.ST_MTIME]))

			md5Str = self.cfmd5.md5sumSmallFile(file, self.path).hexdigest()
			atr[file].append(md5Str)

	def readFileTime(self, atr):
		for file in self.fileNames:
			st = os.stat(self.path + "\\" + file)
			atr[file] = []
			atr[file].append(oct(stat.S_IMODE(st[stat.ST_MODE])))
			atr[file].append(time.ctime(st[stat.ST_MTIME]))
	
	def ServerInitFileDateCheck(self):
		tmpOldName = self.storedFileAtr.keys()
		print "old names: "
		print tmpOldName
		if len(self.storedFileAtr):
			print "kai shi bi jiao"
			print self.fileAtr.keys()
			for file in self.fileAtr.keys():
				print file
				if file in tmpOldName:
					if cmp(self.fileAtr[file][2], self.storedFileAtr[file][2]):
						print "!="
						print "ServerInitFileDateCheck"
						self.updateFileAtr[file] = copy.deepcopy(self.fileAtr[file])
						self.storedFileAtr[file] = copy.deepcopy(self.fileAtr[file])
						continue
				else:
					#self.storedFileAtr[file] = copy.deepcopy(self.fileAtr[file])
					self.updateFileAtr[file] = copy.deepcopy(self.fileAtr[file])

		else :
			print "pei zhi wen jian kong de "
			self.readFileAtr(self.fileAtr)
			self.updateFileAtr = copy.deepcopy(self.fileAtr)

		self.storeFileAte(self.fileAtr)

	def handleFileDateCheck(self):
		tmpFileAtr = {}
		tmpOldName = self.fileAtr.keys()
		self.readFileTime(tmpFileAtr)
		for file in tmpFileAtr.keys():
			if file in tmpOldName :
				if cmp(self.fileAtr[file][1], tmpFileAtr[file][1]):
					md5Str = self.cfmd5.md5sumSmallFile(file, self.path).hexdigest()
					print file
					print "handleFileDateCheck"
					self.fileAtr[file][2] = copy.deepcopy(md5Str)
					self.fileAtr[file][1] = copy.deepcopy(tmpFileAtr[file][1])
					self.updateFileAtr[file] = copy.deepcopy(self.fileAtr[file])
					continue
					

			else :
				self.fileAtr[file] = copy.deepcopy(tmpFileAtr[file])
				md5Str = self.cfmd5.md5sumSmallFile(file, self.path).hexdigest()
				self.fileAtr[file][2] = copy.deepcopy(md5Str)

				self.updateFileAtr[file] = copy.deepcopy(self.fileAtr[file])
	
				
		self.storeFileAte(self.fileAtr)

	def getStoredFileAtr(self):
		try:
			inputf = open('E:\code\server\FileAtr.pkl', 'rb')
			print "da kai pei zhi wen jian cheng gong"
			self.storedFileAtr = pickle.load(inputf)
			
		except:		
			print "pei zhi wen jian chu cuo"
			self.storedFileAtr = {}
		finally:
			inputf.close()

	def storeFileAte(self, fileAtr):
		try:
			output = open('E:\code\server\FileAtr.pkl', 'wb')
			pickle.dump(fileAtr, output, 2)
			
		except IOError:
			print "write file atr failure!"
			sleep(1)
			#os.remove('FileAtr.pkl')
			self.storeFileAte(fileAtr)
		finally :
			output.close()


	def printFileAtr(self):
		print self.fileAtr

	def getFileAtr(self):
		return self.fileAtr
		#print fileAtr
	
if __name__ == '__main__': 
	files = ChechFiles("/home/entouch/emsys/sync_files/server")
	#files.printFileAtr()
	#print files.fileAtr
	print files.updateFileAtr
