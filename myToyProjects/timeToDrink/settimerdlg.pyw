# -*- coding: utf-8 -*-


# 主程序如何最小化到托盘  或许可参考test.py
# pyw执行时 不支持中文

import time, threading
import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ui_SetTimer
import ui_messageDlg

sys.stderr = open("errlog.txt", "w")

class MessageDlg(QDialog,
				ui_messageDlg.Ui_MessageDlg):
	def __init__(self, text, callback, parent=None):
		super(MessageDlg, self).__init__(parent)
		
		#important!!!!!!!!!!!!!!
		self.setupUi(self)
		
		self.messagelabel.setText(text)
		
		self.callback = callback
		
	def on_pushButton_clicked(self):
		print "Ok!!!"
		self.callback()
		self.reject()
			#self.emit(SIGNAL("OkButton"))
			
		#self.connect(self.pushButton, SIGNAL("OkButton"), self.reject)
		
		
	#def reject(self):
		#super(MessageDlg, self).reject()
		#MessageDlg



class SetTimerDlg(QDialog,
				ui_SetTimer.Ui_SetTimerDlg):
	
	def __init__(self, parent=None):
		super(SetTimerDlg, self).__init__(parent)
		
		self.setupUi(self)
		
		#QTextCodec.setCodecForCStrings(QTextCodec.codecForName("GB2312"))
		#QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))
		self.msgDlg = None
		self.sleepTime = 0
		self.circlFlag = False
		self.lineEditFlage = False
		self.timer = QTimer()
		
		#为什么是Qobject？？？不是self了？
		QObject.connect(self.timer, SIGNAL("timeout()"), self.okToContinue)
		QObject.connect(self.timer, SIGNAL("timeout()"), self.nuAlter)
		
		self.MessageTimeEdit.setCurrentSection(self.MessageTimeEdit.SecondSection)
		self.pushButtonEnt.setFocusPolicy(Qt.NoFocus)
		self.pushButtonClear.setFocusPolicy(Qt.NoFocus)
		self.updateUi()
		
	def on_MessageTimeEdit_timeChanged(self):
		self.updateUi()
		self.statuLabel.setText("setting...")
	
	@pyqtSignature("int")
	def on_alterNumber_valueChanged(self):
		print "hello"
		self.updateUi()
		self.statuLabel.setText("Setting...")
	
	@pyqtSignature("QString")
	def on_lineEdit_textChanged(self):
		self.lineEditFlage = True
		self.updateUi()
		self.statuLabel.setText("Setting...")
	
	def on_pushButtonClear_clicked(self):
		timeZero = QTime.fromString("0:00:00", "h:mm:ss")
		self.MessageTimeEdit.setTime(timeZero)
		self.alterNumber.setValue(0)
		self.lineEdit.clear()
		self.checkBox.setChecked(False)
		self.timer.stop()
		self.statuLabel.setText("setting...")
		self.updateUi()
	
	def on_pushButtonHide_clicked(self):
		#self.showMinimized()
		self.setWindowFlags(Qt.WindowModal)
		self.setWindowFlags(Qt.Desktop)
	
	def on_pushButtonEnt_clicked(self):
		self.statuLabel.setText("running...")
		self.getTimeAndSet()
		self.pushButtonEnt.setEnabled(False)
		self.setMessage()

		
		print self.__dateEditHour, self.__dateEditMinute, self.__dateEditSecond, self.__nuAlter
		
	def getTimeAndSet(self):
		self.__dateEditHour = int(self.MessageTimeEdit.sectionText(self.MessageTimeEdit.HourSection))
		self.__dateEditMinute = int(self.MessageTimeEdit.sectionText(self.MessageTimeEdit.MinuteSection))
		self.__dateEditSecond = int(self.MessageTimeEdit.sectionText(self.MessageTimeEdit.SecondSection))
		self.__nuAlter = self.alterNumber.value()
		self.__messagText = unicode(self.lineEdit.text())
		#self.__messagText = self.lineEdit.text()
		self.circlFlag = self.checkBox.isChecked()
		#print self.__nuAlter, self.__messagText
		if self.__dateEditHour or self.__dateEditMinute or self.__dateEditSecond or self.__nuAlter or self.lineEditFlage:
			return True
		else:
			return False
			
	def setMessage(self):
		print "Message"
		self.sleepTime = 3600*self.__dateEditHour + 60*self.__dateEditMinute + self.__dateEditSecond
		self.sleepTime = self.sleepTime * 1000
		if self.__nuAlter or self.circlFlag:
			print self.__nuAlter, self.circlFlag
			#QTimer.singleShot(self.sleepTime, self.okToContinue)
			self.timer.start(self.sleepTime)
			
		else:
			self.pushButtonEnt.setEnabled(True)
			self.timer.stop()
	

	def okToContinue(self):
		if self.msgDlg is None:
			print "msgDlg"
			self.msgDlg = MessageDlg(self.__messagText, self.setMessage, self)
		#self.msgDlg.setAttribute(Qt.WA_DeleteOnClose)
		self.msgDlg.show()
		self.msgDlg.raise_()
		self.msgDlg.activateWindow()
		
	def nuAlter(self):
		print self.__nuAlter
		self.__nuAlter -= 1
		
		
	def updateUi(self):
		enable = self.getTimeAndSet()
		print "enable",enable
		self.pushButtonClear.setEnabled(enable)
		self.pushButtonEnt.setEnabled(enable)
		self.pushButtonHide.setEnabled(enable)
		
	

	

		
if __name__ == "__main__":
	import sys
	
	app = QApplication(sys.argv)
	form = SetTimerDlg()
	form.setWindowModality(Qt.WindowModal)
	form.show()
	
	#QTimer.singleShot(form.sleepTime, form.okToContinue)
	form.exec_()