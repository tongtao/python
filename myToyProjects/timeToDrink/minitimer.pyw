# -*- coding: utf-8 -*-


# 主程序如何最小化到托盘  或许可参考test.py
# pyw执行时 不支持中文  解决 pythonw收115行print影响

import time, threading
import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ui_SetTimer
import ui_messageDlg
import qrc_systray

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
		
		#安装绘制好的界面元素 重要!!!
		self.setupUi(self)
		
		self.msgDlg = None		#消息对话框实例,先初始化为None 便于在实例化前做判断
		self.sleepTime = 0		#提醒间隔时间
		self.circlFlag = False	#是否循环标记,True则提醒次数无限
		self.lineEditFlage = False	#lineEdit内容改变情况标志
		self.timer = QTimer()	#Qtimer实例 用于延迟题型
		
		###################### system tray test area ###########################
		
		#为什么加一个QComboBox???
		#生成个托盘按钮trayIcon,在把它加到iconCombobox中
		self.iconComboBox = QComboBox() #The QComboBox widget is a combined button and popup list
		self.iconComboBox.addItem(QIcon(":/alarm.png"), "Timer")
		
		#生成托盘图标,右键菜单及按钮
		self.minimizeAction = QAction(QIcon(":/circle_minus.png"), u"最小化", self, triggered=self.hide) 
		self.restoreAction = QAction(QIcon(":/circle_play.png"), u"显示窗口", self, triggered=self.showNormal) #widget method
		self.quitAction = QAction(QIcon(":/circle_delete.png"), u"退出", self, triggered=qApp.quit)

		self.trayIconMenu = QMenu(self)
		self.trayIconMenu.addAction(self.restoreAction)
		self.trayIconMenu.addAction(self.minimizeAction)
		self.trayIconMenu.addAction(self.quitAction)
		self.trayIcon = QSystemTrayIcon(self) #The QSystemTrayIcon class can be used on the following platforms
		self.trayIcon.setContextMenu(self.trayIconMenu)
		
		self.iconComboBox.currentIndexChanged.connect(self.setIcon)
		# currentIndexChanged signal is sent when the user chooses an item in the combobox
		# 界面的控件发出的信号 也可以这样与函数连接
		
		self.iconComboBox.setCurrentIndex(1)
		self.trayIcon.show()	#显示托盘
		self.trayIcon.activated.connect(self.iconActivated)  #点击图标的各种响应处理
		

		
		###################### system tray test area ###########################
		
		self.setWindowTitle("Timer")
		
		
		#Qobject或self都可以
		self.connect(self.timer, SIGNAL("timeout()"), self.okToContinue)
		self.connect(self.timer, SIGNAL("timeout()"), self.nuAlter)
		
		self.MessageTimeEdit.setCurrentSection(self.MessageTimeEdit.SecondSection)
		self.pushButtonEnt.setFocusPolicy(Qt.NoFocus)
		self.pushButtonClear.setFocusPolicy(Qt.NoFocus)
		self.updateUi()
		
	###################### system tray test area ###########################
	def iconActivated(self, reason):
		if reason in (QSystemTrayIcon.Trigger,
					  QSystemTrayIcon.DoubleClick):
			self.showNormal()
		elif reason == QSystemTrayIcon.MiddleClick:
			self.showMessage()		
		
	def setIcon(self, index):
		icon = self.iconComboBox.itemIcon(0)
		self.trayIcon.setIcon(icon)
		self.setWindowIcon(icon)
		self.trayIcon.setToolTip(self.iconComboBox.itemText(index))
		
	def showMessage(self):
		#这里是可以设置弹出对话气泡的icon的，作为实验就省略了
		#icon = QSystemTrayIcon.MessageIcon()
		self.showNormal()  # 显示时间设置对话框
		#self.trayIcon.showMessage(
			#u'提示',u'您有新的任务，请注意查收', icon,1000)
			
	def getTasksNum(self):
		self.showMessage()
	###################### system tray test area ###########################
		
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
		self.reject()
		#self.setWindowFlags(Qt.WindowModal)
		#self.setWindowFlags(Qt.Desktop)
	
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
			#self.timer.setSingleShot(True)
			self.timer.start(self.sleepTime)  #一旦设定 timer是反复运行,间隔这个时间发信号
											#当msgDlg按钮后,相当于重新设定时间,重新开始
			
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
	
	app = QApplication(sys.argv)
	QApplication.setQuitOnLastWindowClosed(False)	#不同处 可以阻止Qt应用程序的自动退出。这样可以配合系统托盘实现显示和隐藏程序窗口的功能。 
	form = SetTimerDlg()
	#form.setWindowModality(Qt.WindowModal)
	#form.show()
	form.getTasksNum()	#不同处 直接self.showNormal()即可  这样绕了两此为了显示tip
	
	#QTimer.singleShot(form.sleepTime, form.okToContinue)
	sys.exit(app.exec_())	#不同处