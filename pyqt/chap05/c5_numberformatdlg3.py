# -*- coding: utf-8 -*-

"""
a dialog has no buttons, and where changes are applied automatically and immediately

<validation>
In the modal version of the dialog we used post-mortem validation, and in the
smart modeless version we used a mixture of post-mortem and preventative
validation. In this example, we will use preventative validation exclusively.

<dialog>
Rather than creating the dialog when it is needed and then destroying it, creating and destroying on
every use, we will create it just once, the first time it is needed, and then hide
it when the user is finished with it, showing and hiding on every use.
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def setNumberFormat3(self):
	if self.numberFormatDlg is None:
		self.numberFormatDlg = numberformatdlg3.NumberFormatDlg(
				self.format, self.refreshTable, self)
	self.numberFormatDlg.show()
	self.numberFormatDlg.raise_()
	self.numberFormatDlg.activateWindow()
	# when the dialog is closed it is merely hidden 
	# (because we do not set the Qt.WA_DeleteOnClosewidget attribute)
	# to show a dialog that was created earlier and subsequently hidden
	# we must both raise (put the dialog on top of all the other windows in the application) 
	# and activate (give the focus to the dialog); doing these the first time is harmless

	
class NumberFormatDlg(QDialog):
							# callback ????  keeps a reference to self.refreshTable()in self.callback
	def __init__(self, format, callback, parent=None):
		super(NumberFormatDlg, self).__init__(parent)
		#self.setAttribute(Qt.WA_DeleteOnClose)
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
	
		#buttonBox = QDialogButtonBox(QDialogButtonBox.Apply|QDialogButtonBox.Close)
	
		# In the modal dialog we took a copy of the caller’sformatdictionary; here we
		# take a reference to it, so that we can change it directly from within the dialog.
		self.format = format
		self.callback = callback   # callback ????
		
		grid = QGridLayout()
		grid.addWidget(thousandsLabel, 0, 0)
		grid.addWidget(self.thousandsEdit, 0, 1)
		grid.addWidget(decimalMarkerLabel, 1, 0)
		grid.addWidget(self.decimalMarkerEdit, 1, 1)
		grid.addWidget(decimalPlacesLabel, 2, 0)
		grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
		grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
		#grid.addWidget(buttonBox, 4, 0, 1, 2)
		self.setLayout(grid)
	
		self.connect(self.thousandsEdit, SIGNAL("textEdited(QString)"),
					self.checkAndFix)
		self.connect(self.decimalMarkerEdit, SIGNAL("textEdited(QString)"),
					self.checkAndFix)
		self.connect(self.decimalPlacesSpinBox, SIGNAL("valueChanged(int)"),
					self.apply)
		self.connect(self.redNegativesCheckBox, SIGNAL("toggled(bool)"),
					self.apply)
					
	def apply(self):
		self.format["thousandsseparator"] = unicode(self.thousandsEdit.text())
		self.format["decimalmarker"] = unicode(self.decimalMarkerEdit.text())
		self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
		self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
		self.callback()
		# It no longer emits a signal to announce a state change—instead, 
		# it calls the method it was given and this applies the changes
		# directly to the caller’s form.
		
	def checkAndFix(self):
		thousands = unicode(self.thousandsEdit.text())
		decimal = unicode(self.decimalMarkerEdit.text())
		if thousands == decimal:
			self.thousandsEdit.clear()
			self.thousandsEdit.setFocus()
		if len(decimal) == 0:
			self.decimalMarkerEdit.setText(".")
			self.decimalMarkerEdit.selectAll()
			self.decimalMarkerEdit.setFocus()
		self.apply()
		
