# -*- coding: utf-8 -*-
"""
this smart dialog was modeless and was able to update the
application’s state without being closed,the user could simply invoke the dialog
once, perform their edits, see the effects, and then do more edits, and so on: a
much faster cycle. 
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def setNumberFormat2(self):
	dialog = numberformatdlg2.NumberFormatDlg(self.format, self)
	self.connect(dialog, SIGNAL("changed"), self.refreshTable)
	dialog.show()
	# d.show() Shows QDialog d modelessly
	# d.exec_() Shows QDialog d modally, blocking until it is closed

class NumberFormatDlg(QDialog):
	
	def __init__(self, format, parent=None):
		super(NumberFormatDlg, self).__init__(parent)
		self.setAttribute(Qt.WA_DeleteOnClose)
		# callsetAttribute()to make sure that when the dialog
		# is closed it will be deleted rather than merely hidden.
	
		# QRegExp 正则表达式
		punctuationRe = QRegExp(r"[ ,;:.]")
		# “r” signifies a “raw” string and means that (almost) 
		# all of the characters inside the string are to be taken as literals.  like use "\"
	
		thousandsLabel = QLabel("&Thousands separator")
		self.thousandsEdit = QLineEdit(format["thousandsseparator"])
		thousandsLabel.setBuddy(self.thousandsEdit)
		# this time we are using preventative validation almost exclusively.
		# set a one character maximum length on the thousands separator
		self.thousandsEdit.setMaxLength(1)
		# A validator will only allow the user to enter valid characters, 
		# and in the case of a regular expression validator, 
		# only characters in [ ,;:.] that match the regular expression
		self.thousandsEdit.setValidator(
				QRegExpValidator(punctuationRe, self))
	
		decimalMarkerLabel = QLabel("Decimal &marker")
		self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
		decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
		self.decimalMarkerEdit.setMaxLength(1)
		self.decimalMarkerEdit.setValidator(
				QRegExpValidator(punctuationRe, self))
		# 使Edit控件只允许输入自定义的格式字符串
		# X表示需要一个字符 而字符又由之前的validator限定
		# Although we are happy to accept an empty thousands separator, 
		# we require a decimal marker.
		self.decimalMarkerEdit.setInputMask("X")
	
		decimalPlacesLabel = QLabel("&Decimal places")
		self.decimalPlacesSpinBox = QSpinBox()
		decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
		self.decimalPlacesSpinBox.setRange(0, 6)
		self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
	
		self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
		self.redNegativesCheckBox.setChecked(format["rednegatives"])
	
		buttonBox = QDialogButtonBox(QDialogButtonBox.Apply|QDialogButtonBox.Close)
	
		# In the modal dialog we took a copy of the caller’sformatdictionary; here we
		# take a reference to it, so that we can change it directly from within the dialog.
		self.format = format
		
		grid = QGridLayout()
		grid.addWidget(thousandsLabel, 0, 0)
		grid.addWidget(self.thousandsEdit, 0, 1)
		grid.addWidget(decimalMarkerLabel, 1, 0)
		grid.addWidget(self.decimalMarkerEdit, 1, 1)
		grid.addWidget(decimalPlacesLabel, 2, 0)
		grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
		grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
		grid.addWidget(buttonBox, 4, 0, 1, 2)
		self.setLayout(grid)
	
		# button() Returns the QPushButton corresponding to the standard button which, 
		# or 0 if the standard button doesn't exist in this button box to the button box.
		self.connect(buttonBox.button(QDialogButtonBox.Apply),
					SIGNAL("clicked()"), self.apply)
		self.connect(buttonBox, SIGNAL("rejected()"),
					self, SLOT("reject()"))
				
		self.setWindowTitle("Set Number Format (Modeless)")
		
	def apply(self):
		print "here1"
		thousands = unicode(self.thousandsEdit.text())
		decimal = unicode(self.decimalMarkerEdit.text())
		if thousands == decimal:
			QMessageBox.warning(self, "Format Error",
					"The thousands separator and the decimal marker "
					"must be different.")
			self.thousandsEdit.selectAll()
			self.thousandsEdit.setFocus()
			return
		if len(decimal) == 0:
			QMessageBox.warning(self, "Format Error",
								"The decimal marker may not be empty.")
			self.decimalMarkerEdit.selectAll()
			self.decimalMarkerEdit.setFocus()
			return
		print "here2"
		self.format["thousandsseparator"] = thousands
		self.format["decimalmarker"] = decimal
		self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
		self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
		self.emit(SIGNAL("changed"))
		# emit a changed signal, and as we have seen, 
		# this causes the caller’s refreshTable()method to be called