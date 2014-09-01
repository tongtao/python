# -*- coding: utf-8 -*-

#更改bookInfostore数据的结构


import time
import sys
import os	#用于取文件夹下信息
import pickle	#用于将信息保存到文件
from PyQt4.QtCore import*
from PyQt4.QtGui import*

import ui_bookManagerWindow
import ui_fileInfoEdit

class fileInfoEdit(QDialog,
				ui_fileInfoEdit.Ui_fileInfoEdit):
	def __init__(self, info, text, callback, parent=None):
		super(fileInfoEdit, self).__init__(parent)
		self.setupUi(self)
		
		self.callback = callback
		
		self.set(info, text)
		
		
	def set(self, info, text):
		self.info = info
		self.text = text
		
		self.lineEditCurPages.setText(self.info['curPages'])
		self.lineEditAllPages.setText(self.info['allPages'])
		self.lineEditReadTimes.setText(self.info['readTimes'])
		self.lineEditPro.setText(self.info['pro'])
		self.textEditModify.clear()
		self.textEditModify.append(self.text)
		self.pushButtonEnt.setEnabled(False)
		
		
		
	@pyqtSignature("QString")
	def on_lineEditCurPages_textChanged(self):
		self.pushButtonEnt.setEnabled(True)
			
	@pyqtSignature("QString")
	def on_lineEditAllPages_textChanged(self):
		self.pushButtonEnt.setEnabled(True)
			
	@pyqtSignature("QString")
	def on_lineEditReadTimes_textChanged(self):
		self.pushButtonEnt.setEnabled(True)
		
	@pyqtSignature("QString")
	def on_lineEditPro_textChanged(self):
		self.pushButtonEnt.setEnabled(True)
			
	def on_textEditModify_cursorPositionChanged(self):
		self.pushButtonEnt.setEnabled(True)
			
	def on_pushButtonEnt_clicked(self):
		self.info['curPages'] = self.lineEditCurPages.text()
		self.info['allPages'] = self.lineEditAllPages.text()
		self.info['readTimes'] = self.lineEditReadTimes.text()
		self.info['pro'] = self.lineEditPro.text()
		self.info['text'] = self.textEditModify.toPlainText()
		#self.text = self.textEditModify.toPlainText()
		#print "%s" % self.text
		self.pushButtonEnt.setEnabled(False)
		self.callback()

class bookManager(QMainWindow,
				ui_bookManagerWindow.Ui_bookManager):
	def __init__(self, parent=None):
		super(bookManager, self).__init__(parent)
		
		self.setupUi(self)
		

		
		self.setCentralWidget(self.bookTree)
		
		# 设定列头的伸缩模式
		self.bookTree.header().setResizeMode(0, QHeaderView.ResizeToContents)
		self.bookTree.header().setResizeMode(1, QHeaderView.ResizeToContents)
		self.bookTree.header().setResizeMode(2, QHeaderView.ResizeToContents)
		
		# 设定背景颜色
		color = self.bookTree.palette()
		color.setColor(QPalette.Base, QColor(192,192,192))
		self.bookTree.setPalette(color)
		
		self.readDirInfo()
		self.fileUseInfo = {}
		self.creatUseInfo()
		self.useInfoEdit = None		
		
		#测试用,稍后删
		self.syncTree()
		
		# 创建Dock Widget并加入 textEdit
		infoDockWidget = QDockWidget("Info", self)
		infoDockWidget.setObjectName("InfoDockWidget")
		infoDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
		self.textEdit = QTextEdit()
		infoDockWidget.setWidget(self.textEdit)
		self.addDockWidget(Qt.RightDockWidgetArea, infoDockWidget)

		# 更新文件树
		self.actionSyncTree.triggered.connect(self.syncTree)
		# 打开选中文件
		self.actionOpenFile.triggered.connect(self.openSelectedFile)
		# 单击显示文件注释
		self.bookTree.itemDoubleClicked.connect(self.showSelectedFileInfo)
		# 文件信息编辑
		self.actionEdit.triggered.connect(self.editUseInfo)
		

	
	# 根据配置文件和读取的文件夹信息 生成文件信息
	def creatUseInfo(self):
		
		try:
			input = open('useInfo.pkl', 'rb')
			self.fileUseInfo = pickle.load(input)
			input.close()
			
			for file in self.dirInfo.dirInfoStore.keys():
				if file not in self.fileUseInfo.keys():
					self.fileUseInfo[file] = {'curPages': '0', 'allPages': '0',
										'readTimes': '0', 'pro': '1'}
		except IOError:
			for file in self.dirInfo.dirInfoStore.keys():
				self.fileUseInfo[file] = {'curPages': '0', 'allPages': '0',
										'readTimes': '0', 'pro': '1'}
	
	# 文件信息编辑
	def editUseInfo(self):
		self.SelectedFile()
		
		try:
			self.text = self.readInfoText(self.selectFileName1.encode('GBK'))
			self.text = unicode(self.text, 'UTF-8', 'ignore')
		except IOError:
			self.text = u"内容为空"
		finally:
			if self.useInfoEdit is None:
				self.useInfoEdit = fileInfoEdit(self.fileUseInfo[self.selectFileName1], 
								self.text, self.refresh, self)
			else:	
				self.useInfoEdit.set(self.fileUseInfo[self.selectFileName1], self.text)
			self.useInfoEdit.show()
			self.useInfoEdit.raise_()
			self.useInfoEdit.activateWindow()
		
	def refresh(self):
		curPages = float(self.fileUseInfo[self.selectFileName1]['curPages'])
		allPages = float(self.fileUseInfo[self.selectFileName1]['allPages'])
		readTimes = self.fileUseInfo[self.selectFileName1]['readTimes']
		if allPages > 0:
			pace = "(%d%%, %s)" % (curPages/allPages*100, readTimes)
		else:
			pace = "(0%, 0)"
		self.selectedFileItem.setText(1, pace)
		
		output = open('useInfo.pkl', 'wb')
		pickle.dump(self.fileUseInfo, output, 2)
		output.close()
		
		self.writeInfoText(self.selectFileName1)
		
		
		
	def SelectedFile(self):
		
		self.selectedFileItem = self.bookTree.selectedItems().pop()
		#返回的是个item的list  这里因为只选一个  就取第一个
		selectFileName = self.selectedFileItem.text(0)
		self.selectFileName1 = "%s" % selectFileName
		self.selectFileName = selectFileName
		self.selectFileName = selectFileName
		print "%s" % selectFileName
		filePath = u"E:\暑假学习\计算机基础"
		
		fileParent = self.selectedFileItem.parent().text(0)
		
		while self.selectedFileItem.parent().text(0) != self.dirInfo.rootfile:
			self.selectedFileItem = self.selectedFileItem.parent()
			selectFileName = self.selectedFileItem.text(0)+"\\"+selectFileName
		print "%s" % selectFileName
		
		absFilePath = "%s\\%s" % (filePath, selectFileName)
		self.selectedFileItem = self.bookTree.selectedItems().pop()
		
		self.fileParent = fileParent
		self.absFilePath = absFilePath
		
	
	def openSelectedFile(self):
		self.SelectedFile()
		self.openFile(self.absFilePath.encode('GBK'))


	def openFile(self, path):
		runComand = "D:\Program Files\Foxit Software\Foxit Reader\Foxit Reader.exe"
		cmd_args = [runComand, path]
		
		import subprocess
		subprocess.Popen(cmd_args)
	
	def showSelectedFileInfo(self):
		self.SelectedFile()
		self.showFileInfo()
		
	def showFileInfo(self):
		self.textEdit.clear()
		try:
			text = self.readInfoText(self.selectFileName1.encode('GBK'))
		except IOError:
			text = "内容为空"
		finally:
			infoTitle = u"""
						<p>
							<span style="font-family:Microsoft YaHei;"><span style="font-size:12px;">{0}</span><span style="font-size:18px;"><span style="font-size:14px;"></span></span></span>
						</p>
						""".format(self.selectFileName)
			infoText = 	u"""
						<p>
							<span style="font-family:Microsoft YaHei;"><span style="font-size:12px;">{0}</span><span style="font-size:18px;"><span style="font-size:14px;"></span></span></span>
						</p>
						""".format(unicode(text, 'UTF-8', 'ignore'))
		
			self.textEdit.acceptRichText()
			self.textEdit.setReadOnly(True)
			self.textEdit.append(infoTitle)
			self.textEdit.append(infoText)
		
	# 读取制定txt文件
	def readInfoText(self, file):
		fileInfoPath = "Info\\%s.bm" % file
		
		fp = open(fileInfoPath, 'r')
		text = fp.read()
		print type(text)
		fp.close()
		
		return text
		
	def writeInfoText(self, file):
		fileInfoPath = u"Info\\%s.bm" % file
		
		fo = open(fileInfoPath, 'w')
		try:
			text =  self.fileUseInfo[self.selectFileName1].pop('text')
			#print type(text)
			#text = unicode(text, 'GBK', 'ignore')
			#print type(text)
			
			#fo.write(text)
			fo.seek(0)
			fo.write(unicode(text).encode('utf-8'))
			fo.flush()
			
			print "%s write OK" % text
		except:
			print "error"
		finally:
			fo.close()
		
		
	#生成树
	def syncTree(self):
		self.root = QTreeWidgetItem(self.bookTree)
		self.root.setText(0, self.dirInfo.rootfile)
		
		self.addItem(self.root, self.dirInfo.rootfile)
		
					#传入父节点的item, 和父节点的名字, 以递归的生成子文件tree
	
	# 为树加节点
	def addItem(self, parent, name):
	
		# 设置item的图标
		dirIcon = QIcon()
		dirIcon.addPixmap(QPixmap(QString.fromUtf8("images/folder.png")), QIcon.Normal, QIcon.Off)
		documentIcon = QIcon()
		documentIcon.addPixmap(QPixmap(QString.fromUtf8("images/document.png")), QIcon.Normal, QIcon.Off)
		
		# 遍历文件夹name下的文件
		for file in self.dirInfo.dirInfoStore[name]['contain']:
			child = QTreeWidgetItem(parent)
			
			if self.dirInfo.dirInfoStore[file]['isDir']:
				child.setText(0, file)
				child.setIcon(0, dirIcon)
				self.addItem(child, file)
			else:
				child.setText(0, file)
				curPages = float(self.fileUseInfo[file]['curPages'])
				allPages = float(self.fileUseInfo[file]['allPages'])
				readTimes = self.fileUseInfo[file]['readTimes']
				if allPages > 0:
					pace = "(%d%%, %s)" % (curPages/allPages*100, readTimes)
				else:
					pace = "(0%, 0)"
				child.setText(1, pace)
				#filePace = "(%s%%, %s)" % (self.dirInfo.dirInfoStore[file]['pace'][0],
											#self.dirInfo.dirInfoStore[file]['pace'][1])
				#child.setText(1, filePace)
				child.setText(2, self.dirInfo.dirInfoStore[file]['time'])
			

	def readDirInfo(self):
		#dirPath = r"E:\code\tools\bookManager\demo"
		dirPath = u"E:\暑假学习\计算机基础"
		
		self.dirInfo = readDirInfo(dirPath)

		# 读取制定文件夹下的文件信息
class readDirInfo():
	def __init__(self, dirPath):
		self.dirPath = dirPath
		
		self.dirInfoStore = {}
		self.rootfile = self.dirPath.split('\\').pop()	#获取根文件名
		
		self.readDir(self.dirPath)
	
	def readDir(self, path):
		files = os.listdir(path)
		dirName = path.split('\\').pop()
		#self.dirInfoStore[dirName] = {}
		#dirName = "%s" % dirName
		if dirName == self.rootfile:
			self.dirInfoStore[dirName] = {}
			self.dirInfoStore[dirName]['contain'] = []
			self.dirInfoStore[dirName]['isDir'] = True
			self.dirInfoStore[dirName]['parent'] = None
		
		for file in files:
			fullNmae = os.path.join(path, file)
			
			self.dirInfoStore[dirName]['contain'].append(file)
			
			#取得文件最后打开时间,并设定格式
			statinfo = os.stat(fullNmae)
			fileAdate = time.localtime(statinfo.st_atime)
			fileAdateFomat = time.strftime("%Y/%m/%d %H:%M", fileAdate) 
			
			if os.path.isdir(fullNmae):
				#self.dirInfoStore["%s" % dirName].append({"name": file, 
								#"time": fileAdateFomat, "isDir": True})
				self.dirInfoStore[file] = {}
				self.dirInfoStore[file]['isDir'] = True
				self.dirInfoStore[file]['parent'] = dirName
				self.dirInfoStore[file]['contain'] = []
				self.readDir(fullNmae)
			else:
				#self.dirInfoStore["%s" % dirName].append({"name": file, 
								#"time": fileAdateFomat, "isDir": False})
				self.dirInfoStore[file] = {}
				self.dirInfoStore[file]['isDir'] = False
				self.dirInfoStore[file]['parent'] = dirName
				self.dirInfoStore[file]['time'] = fileAdateFomat
				self.dirInfoStore[file]['pace'] = [0, 0]
				
if __name__ == "__main__":

	app = QApplication(sys.argv)
	bWindow = bookManager()
	bWindow.show()
	app.exec_()