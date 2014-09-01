# -*- coding: utf-8 -*-

from __future__ import division   # division:精确的除法
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# create a top-level window we subclass QDialog,or QMainWindow or occasionally,QWidget
# inheriting QDialogwe get a blank form
class Form(QDialog):
	#  A widget that has no parent becomes a top-level window, which is what we want for our form.
	def __init__(self, parent=None):
		# super() only works for new-style classes. 用于调用父类的方法
		super(Form, self).__init__(parent)
		# create the two widgets
		self.browser = QTextBrowser()
		self.lineedit = QLineEdit("Type an expression and press Enter")
		self.lineedit.selectAll()
		
		# We want the widgets to appear vertically, one above the other
		# by creating a QVBoxLayout and adding our two widgets to it, and
		# then setting the layout on the form
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.setLayout(layout)
		# the focus to start in theQLineEdit
		self.lineedit.setFocus()
		self.connect(self.lineedit, SIGNAL("returnPressed()"),
				self.updateUi)
		self.setWindowTitle("Calulate")
		
	def updateUi(self):
		try:
			# retrieves the text from the PyQt string immediately converting it to a unicodeobject
			text = unicode(self.lineedit.text())
			# eval()function to evaluate the string as an expression
			self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
			self.lineedit.clear()
		except:
			self.browser.append(
					"<font color=red>%s is invalid!</font" % text)
			self.lineedit.clear()
						
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()