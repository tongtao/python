# -*- coding: utf-8 -*-

import urllib2
import re
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ui_findandreplacedlg

MAC = True
try:
	from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
	MAC = False

# The first class we inherit isQDialog. If we were using the “Widget” template 
# our first inherited class would beQWidget, and if we were
# using the “Main Window” template our first inherited class would beQMainWindow. 
# The second class we inherit is the class that represents the user interface
# we designed usingQt Designer.


class FindAndReplaceDlg(QDialog,
		ui_findandreplacedlg.Ui_FindAndReplaceDlg):
	
	def __init__(self, text, parent=None):
		# The super()call is made on the first inherited class, QDialog
		super(FindAndReplaceDlg, self).__init__(parent)
		# keep a copy of the text, and also an index position, in case the user
		# clicksFindmore than once to find subsequent occurrences of the same text.
		self.__text = unicode(text)
		self.__index = 0
		# setupUi() re-creates the form we designed inQt Designer
		self.setupUi(self)
		if not MAC:
			self.findButton.setFocusPolicy(Qt.NoFocus)
			self.replaceButton.setFocusPolicy(Qt.NoFocus)
			self.replaceAllButton.setFocusPolicy(Qt.NoFocus)
			self.closeButton.setFocusPolicy(Qt.NoFocus)
			self.updateUi()
	# the setupUi() method calls QtCore.QMetaObject.connectSlotsByName(), a static method that creates signal–slot connections between form
	# widget signals and methods in our subclass that follow a particular naming
	# convention. Any method whose name is of the formon_widgetName_signalName
	# will have the named widget’s named signal connected to it
	# Whenever we want an automatic connection we use the @pyqtSignature decorator to specify the signal’s arguments.
	# The purpose of the decorator is to distinguish between signals that have the same name but different parameters.
	@pyqtSignature("QString")
	def on_findLineEdit_textEdited(self, text):
		self.__index = 0
		self.updateUi()
	
	# This method is the reason why the form starts with every button except the Close button disabled.	
	def updateUi(self):
		enable = not self.findLineEdit.text().isEmpty()
		self.findButton.setEnabled(enable)
		self.replaceButton.setEnabled(enable)
		self.replaceAllButton.setEnabled(enable)
	
	# the text it holds (which may be different from the original text 
	# if the user has used replace or replace all) is accessible using the text() method.
	def text(self):
		return self.__text
		
	@pyqtSignature("")
	def on_findButton_clicked(self):
		regex = self.makeRegex()
		match = regex.search(self.__text, self.__index)
		if match is not None:
			self.__index = match.end()
			self.emit(SIGNAL("found"), match.start())
		else:
			self.emit(SIGNAL("notfound"))
	
	# getting the find text that the user has entered
	def makeRegex(self):
		findText = unicode(self.findLineEdit.text())
		if unicode(self.syntaxComboBox.currentText()) == "Literal":
			findText = re.escape(findText)
		flags = re.MULTILINE|re.DOTALL|re.UNICODE
		if not self.caseCheckBox.isChecked():
			flags |= re.IGNORECASE
		if self.wholeCheckBox.isChecked():
			findText = r"\b%s\b" % findText
		return re.compile(findText, flags)
		
	@pyqtSignature("")
	def on_replaceButton_clicked(self):
		regex = self.makeRegex()
		self.__text = regex.sub(unicode(self.replaceLineEdit.text()),
							self.__text, 1)
							
	@pyqtSignature("")
	def on_replaceAllButton_clicked(self):
		regex = self.makeRegex()
		self.__text = regex.sub(unicode(self.replaceLineEdit.text()),
							self.__text)
							
if __name__ == "__main__":
	import sys

	text = """US experience shows that, unlike traditional patents,
software patents do not encourage innovation and R&D, quite the
contrary. In particular they hurt small and medium-sized enterprises
and generally newcomers in the market. They will just weaken the market
and increase spending on patents and litigation, at the expense of
technological innovation and research. Especially dangerous are
attempts to abuse the patent system by preventing interoperability as a
means of avoiding competition with technological ability.
--- Extract quoted from Linus Torvalds and Alan Cox's letter
to the President of the European Parliament
http://www.effi.org/patentit/patents_torvalds_cox.html"""

	fh = urllib2.urlopen("http://www.mnsfz.com/h/yangguang/PHPdambCPiCPPPbHH.html")


	def found(where):
		print("Found at {0}".format(where))

	def nomore():
		print("No more found")

	app = QApplication(sys.argv)
	form = FindAndReplaceDlg(text)
	form.connect(form, SIGNAL("found"), found)
	form.connect(form, SIGNAL("notfound"), nomore)
	form.show()
	app.exec_()
	print(form.text())
