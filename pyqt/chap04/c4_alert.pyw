# -*- coding: utf-8 -*-

import sys        #access the command-line arguments it holds in the sys.argvlist
import time       #sleep()function
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Every PyQt GUI application must have aQApplication object
# This object provides access to global-like information such as 
# the application’s directory, the screen size (and which screen the
# application is on, in a multihead system), event loop and so on
# create aQApplicationobject we pass it the command-line arguments
app = QApplication(sys.argv)

try:
	#set the due variable to the time right now
	due = QTime.currentTime()
	message = "Alert!"
	
	if len(sys.argv) < 2:
		raise ValueError
		
	hours, mins = sys.argv[1].split(":")
	due = QTime(int(hours), int(mins))
	if not due.isValid():
		raise ValueError
		
	# set the message to be the space-separated concatenation
	# of the other command-line arguments if there are any
	if len(sys.argv) > 2:
		message = " ".join(sys.argv[2:])
		
except ValueError:
	message = "Usage: alert.pyw HH:MM [optional message]"
	
while QTime.currentTime() < due:
	time.sleep(20)
	
label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
# set the label’s window flags to those used for splash screens since they have no title bar
label.setWindowFlags(Qt.SplashScreen)
# The call to show() merely schedules a “paint event”
# it adds a new event to the QApplication object’s event queue 
# that is a request to paint the specified widget
label.show()
# a timer time out event that wants to take place in a minute’s time
QTimer.singleShot(60000, app.quit) # 1 minute
# now we have two events scheduled
# app.exec_()starts off theQApplicationobject’s event loop
app.exec_()
# The first event it gets is the paint event
# About one minute later the timer time out event occurs 
# and the QApplication.quit()method is called	

