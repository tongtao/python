# -*- coding: utf-8 -*-
# sometimes we want to connect two or more signals to the same slot, 
# and have the slot behave differently depending on who called it.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		button1 = QPushButton("one")
		button2 = QPushButton("two")
		button3 = QPushButton("three")
		button4 = QPushButton("four")
		button5 = QPushButton("five")
		
		self.buttonLabel = QLabel("You have not clicked")
		
		layout = QHBoxLayout()
		layout.addWidget(button1)
		layout.addWidget(button2)
		layout.addWidget(button3)
		layout.addWidget(button4)
		layout.addWidget(button5)
		layout.addStretch()
		layout.addWidget(self.buttonLabel)
		self.setLayout(layout)
		
		self.setWindowTitle("connections")
		
		self.connect(button1, SIGNAL("clicked()"), self.one)
		self.connect(button2, SIGNAL("clicked()"), self.two)
		self.connect(button3, SIGNAL("clicked()"), self.three)
		self.connect(button4, SIGNAL("clicked()"), self.four)
		self.connect(button5, SIGNAL("clicked()"), self.five)
		
	def one(self):
		self.buttonLabel.setText("You clicked button 'one'")
		
	def two(self):
		self.buttonLabel.setText("You clicked button 'two'")
		
	def three(self):
		self.buttonLabel.setText("You clicked button 'three'")
		
	def four(self):
		self.buttonLabel.setText("You clicked button 'four'")
		
	def five(self):
		self.buttonLabel.setText("You clicked button 'five'")
		
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()