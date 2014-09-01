# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		dial = QDial()
		dial.setNotchesVisible(True)
		
		self.spinbox = ZeroSpinBox()
		self.zeroLabel = QLabel("zeros=0")
		
		layout = QHBoxLayout()
		layout.addWidget(dial)
		layout.addWidget(self.spinbox)
		layout.addWidget(self.zeroLabel)
		self.setLayout(layout)
		
		self.setWindowTitle("signal, slots, emit")
		
		self.connect(dial, SIGNAL("valueChanged(int)"),
					self.spinbox.setValue)
		self.connect(self.spinbox, SIGNAL("valueChanged(int)"),
					dial.setValue)
		self.connect(self.spinbox, SIGNAL("atzero"), self.showZeros)
		
	#def showZeros(self):
		#self.zeroLabel.setText("%d" % self.spinbox.zeros)
	# the function checkzero() passing additional data like this is optional
	def showZeros(self, zeros):
		self.zeroLabel.setText("zeros=%d" % zeros)
					
class ZeroSpinBox(QSpinBox):
	
	zeros = 0
	
	def __init__(self, parent=None):
		super(ZeroSpinBox, self).__init__(parent)
		self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)
	
	# If the value happens to be 0, the checkzero() slot emits the
	# atzero signal, along with a count of how many times it has been zero
	# passing additional data like this is optional
	def checkzero(self):
		if self.value() == 0:
			self.zeros += 1
			self.emit(SIGNAL("atzero"), self.zeros)
					
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()