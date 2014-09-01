# -*- coding: utf-8 -*-
"""
an application that needs to display a table of
floating-point numbers, and that we want to give users some control over the
format of the numbers
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# The data that we want the dialog to make available to the user is 
# held in a dictionary in the main form like this is very convenient, 
# and makes it easy to add additional items
"""
self.format = dict(thousandsseparator=",",
					decimalmarker=".", 
					decimalplaces=2,
					rednegatives=False)
"""
					
class NumberFormatDlg(QDialog):
	"""
	__init__()	accept()	numberFormat()
	"""
	
	
	def __init__(self, format, parent=None):
		super(NumberFormatDlg, self).__init__(parent)
		# The__init__()method begins in the same way as all the other dialogs we have seen so far
		
		thousandsLabel = QLabel("&Thousands separator")
		self.thousandsEdit = QLineEdit(format["thousandsseparator"])
		thousandsLabel.setBuddy(self.thousandsEdit)
		decimalMarkerLabel = QLabel("Decimal &marker")
		self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
		decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
		decimalPlacesLabel = QLabel("&Decimal places")
		self.decimalPlacesSpinBox = QSpinBox()
		decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
		self.decimalPlacesSpinBox.setRange(0, 6)
		self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
		self.redNegativesCheckBox = QCheckBox("&Red negative numbers")
		self.redNegativesCheckBox.setChecked(format["rednegatives"])
		
		# this time we have aQDialogButtonBoxwidget rather than
		# a layout for the buttons.This makes it possible to create 
		# the entire layout using a singleQGridLayout.
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
									QDialogButtonBox.Cancel)
									
		self.format = format.copy()
		
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
		
		self.connect(buttonBox, SIGNAL("accepted()"),
					self, SLOT("accept()"))
		self.connect(buttonBox, SIGNAL("rejected()"),
					self, SLOT("reject()"))
		self.setWindowTitle("Set Number Format (Modal)")
	
	
	# it is possible that some of the editing widgets contain invalid data. To handle this,
	# we reimplement QDialog.accept() and do our validation here
	def accept(self):
		class ThousandsError(Exception): pass
		class DecimalError(Exception): pass
		Punctuation = frozenset(" ,;:.")
		
		# begin by getting the text from the two line edits
		thousands = unicode(self.thousandsEdit.text())
		decimal = unicode(self.decimalMarkerEdit.text())
		
		try:
			if len(decimal) == 0:
				# raise our customDecimalError with suitable error text
				raise DecimalError, ("The decimal marker may not be empty.")
			if len(thousands) > 1:
				raise ThousandsError, ("The thousands separator may only be empty or one character.")
			if len(decimal) > 1:
				raise DecimalError, ("The decimal marker must be one character")
			if thousands == decimal:
				raise ThousandsError, ("The thousands separator and the decimal marker must be different.")
			if thousands and thousands not in Punctuation:
				raise ThousandsError, ("The thousands separator must be a punctuation symbol.")
			if decimal not in Punctuation:
				raise DecimalError, ("The decimal marker must be a punctuation symbol.")
		
		# e 是raise 后括号里的内容 must convert the exception objecte to be a string by use unicode()
		except ThousandsError, e:
			QMessageBox.warning(self, "Thousands Separator Error",
								unicode(e))
			self.thousandsEdit.selectAll()
			self.thousandsEdit.setFocus()
			return
		
		except DecimalError, e:
			QMessageBox.warning(self, "Decimal Marker Error",
								unicode(e))
			self.decimalMarkerEdit.selectAll()
			self.decimalMarkerEdit.setFocus()
			return
		# return—so the dialog is not accepted and the user must 
		# either fix the problem or clickCancelto close
		# the dialog and abandon their changes.
			
		self.format["thousandsseparator"] = thousands
		self.format["decimalmarker"] = decimal
		self.format["decimalplaces"] = (
				self.decimalPlacesSpinBox.value())
		self.format["rednegatives"] = (
				self.redNegativesCheckBox.isChecked())
		QDialog.accept(self)  #  call the base class’s accept() method
		# The form will be closed (i.e., hidden) and a True value returned from theexec_() statement.
	
	def numberFormat(self):
		return self.format
		
"""
Creating modal dialogs like this one above is usually straightforward. The only
complications involved concern whether we have layouts and validation that
require some care to get right, as we do here.
"""
		
def setNumberFormat1(self):
	dialog = numberformatdlg1.NumberFormatDlg(self.format, self)
	if dialog.exec_(): 
	# In the next section, we will use modeless versions of the dialog 
	# that don’t impose this restriction.
		self.format = dialog.numberFormat()
		self.refreshTable()
		
	
	
