# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PenPropertiesDlg(QDialog):
	
	def __init__(self, parent=None):
		super(PenPropertiesDlg, self).__init__(parent)
		
		# text of "&Width:" will appear as Width(W带下划线): and its accelerator will be Alt+W
		# What distinguishes between a literal ampersand and an accelerator ampersand is if 
		# the label has a “buddy”: If it does, the ampersand signifies an accelerator
		widthLabel = QLabel("&Width:")
		self.widthSpinBox = QSpinBox()
		# A buddy is a widget that PyQt will pass the keyboard focus to when the
		# corresponding label’s accelerator is pressed
		widthLabel.setBuddy(self.widthSpinBox)
		self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
		self.widthSpinBox.setRange(0, 24)
		
		self.beveledCheckBox = QCheckBox("&Beveled edges")
		styleLabel = QLabel("&Style:")
		self.styleComboBox = QComboBox()
		styleLabel.setBuddy(self.styleComboBox)
		self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])
		# the user can press the button by clicking it with the mouse, by tabbing to it
		# and pressing the spacebar, or by pressing Alt+O.
		okButton = QPushButton("&OK")
		cancelButton = QPushButton("Cancel")
		
		buttonLayout = QHBoxLayout()
		# The stretch will consume as much space as possible,which has the effect of 
		# pushing the two buttons as far to the right as they can go, and still fit.
		buttonLayout.addStretch()
		buttonLayout.addWidget(okButton)
		buttonLayout.addWidget(cancelButton)
		layout = QGridLayout()
		layout.addWidget(widthLabel, 0, 0)
		layout.addWidget(self.widthSpinBox, 0, 1)
		layout.addWidget(self.beveledCheckBox, 0, 2)
		layout.addWidget(styleLabel, 1, 0)
		# The arguments to the QGridLayout.addWidget()method are the widget, the row, 
		# the column, and then optionally, the number of rows to span, followed by 
		# the number of columns to span
		layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
		# take notice this addLayout()
		layout.addLayout(buttonLayout, 2, 0, 1, 3)
		self.setLayout(layout)
		
		self.connect(okButton, SIGNAL("clicked()"), self, SLOT("accept()"))
		self.connect(cancelButton, SIGNAL("clicked()"), self, SLOT("reject()"))
		self.setWindowTitle("Pen Properties")
		
class Form(QDialog):
	
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		self.width = 1
		self.beveled = False
		self.style = "Solid"
		
		penButtonInline = QPushButton("Set Pen...(Dumb &inline)")
		penButton = QPushButton("Set Pen... (Dumb &class)")
		self.label = QLabel("The Pen has not been set")
		self.label.setTextFormat(Qt.RichText)
		#RichText 设定为多信息文本 HTML风格标记的
		
		layout = QVBoxLayout()
		layout.addWidget(penButtonInline)
		layout.addWidget(penButton)
		layout.addWidget(self.label)
		self.setLayout(layout)
		
		self.connect(penButtonInline, SIGNAL("clicked()"),
					self.setPenInline)
		self.connect(penButton, SIGNAL("clicked()"),
					self.setPenProperties)
					
		self.setWindowTitle("pen")
		
		#self.updateData()
		
	
	def updateData(self):
		bevel = ""
		if self.beveled:
			# <br> 表换行
			bevel = "<br>Beveled"
			# HTML 格式输出
		self.label.setText("Width = {0}<br>Style = {1}{2}".format(
							self.width, self.style, bevel))

	# Creating dialogs inline is not an approach that we would recommend, 
	# so we will not review the code for doing it, but it is mentioned 
	# and provided in the example’ssetPenInline() method for completeness
	def setPenInline(self):
		widthLabel = QLabel("&Width:")
		widthSpinBox = QSpinBox()
		widthLabel.setBuddy(widthSpinBox)
		widthSpinBox.setAlignment(Qt.AlignRight)
		widthSpinBox.setRange(0, 24)
		widthSpinBox.setValue(self.width)
		beveledCheckBox = QCheckBox("&Beveled edges")
		beveledCheckBox.setChecked(self.beveled)
		styleLabel = QLabel("&Style:")
		styleComboBox = QComboBox()
		styleLabel.setBuddy(styleComboBox)
		styleComboBox.addItems(["Solid", "Dashed", "Dotted",
								"DashDotted", "DashDotDotted"])
		styleComboBox.setCurrentIndex(styleComboBox.findText(self.style))
		okButton = QPushButton("&OK")
		cancelButton = QPushButton("Cancel")

		buttonLayout = QHBoxLayout()
		buttonLayout.addStretch()
		buttonLayout.addWidget(okButton)
		buttonLayout.addWidget(cancelButton)
		layout = QGridLayout()
		layout.addWidget(widthLabel, 0, 0)
		layout.addWidget(widthSpinBox, 0, 1)
		layout.addWidget(beveledCheckBox, 0, 2)
		layout.addWidget(styleLabel, 1, 0)
		layout.addWidget(styleComboBox, 1, 1, 1, 2)
		layout.addLayout(buttonLayout, 2, 0, 1, 3)

		form = QDialog()
		form.setLayout(layout)
		self.connect(okButton, SIGNAL("clicked()"),
					form, SLOT("accept()"))
		self.connect(cancelButton, SIGNAL("clicked()"),
					form, SLOT("reject()"))
		form.setWindowTitle("Pen Properties")

		if form.exec_():
			self.width = widthSpinBox.value()
			self.beveled = beveledCheckBox.isChecked()
			self.style = unicode(styleComboBox.currentText())
			self.updateData()							

	def setPenProperties(self):
		dialog = PenPropertiesDlg(self)
		dialog.widthSpinBox.setValue(self.width)
		dialog.beveledCheckBox.setChecked(self.beveled)
		dialog.styleComboBox.setCurrentIndex(
				dialog.styleComboBox.findText(self.style))
				# QComboBox.findText() returns the index position of the item with the matching text
		# The exec_() return value evaluates to
		# True if the user accepted the dialog; otherwise, it evaluates to False
		if dialog.exec_():
			self.width = dialog.widthSpinBox.value()
			self.beveled = dialog.beveledCheckBox.isChecked()
			self.style = unicode(dialog.styleComboBox.currentText())
			self.updateData()
		
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()