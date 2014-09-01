# -*- coding: utf-8 -*-

import sys
import urllib2    #provides a very useful convenience function that makes it easy to grab a file over the Internet
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

	def __init__(self,  parent=None):
		super(Form, self).__init__(parent)
		
		date = self.getdata()
		rates = sorted(self.rates.keys())
		
		dateLabel = QLabel(date)
		# we do need to access the comboboxes and toLabel
		# so we make these instance variables by using self
		self.fromComboBox = QComboBox()
		self.fromComboBox.addItems(rates)
		self.fromSpinBox = QDoubleSpinBox()
		# provide a minimum and maximum value for the spinbox, and also an initial value
		self.fromSpinBox.setRange(0.01, 10000000.00)
		self.fromSpinBox.setValue(1.00)
		self.toComboBox = QComboBox()
		self.toComboBox.addItems(rates)
		self.toLabel = QLabel("1.00")
		
		# we add a widget to a grid we give the row and column position it should occupy,
		# both of which are 0-based
		grid = QGridLayout()
		grid.addWidget(dateLabel, 0, 0)
		grid.addWidget(self.fromComboBox, 1, 0)
		grid.addWidget(self.fromSpinBox, 1, 1)
		grid.addWidget(self.toComboBox, 2, 0)
		grid.addWidget(self.toLabel, 2, 1)
		self.setLayout(grid)

		self.connect(self.fromComboBox,
				SIGNAL("currentIndexChanged(int)"), self.updateUi)
		self.connect(self.toComboBox,
				SIGNAL("currentIndexChanged(int)"), self.updateUi)
		self.connect(self.fromSpinBox,
				SIGNAL("valueChanged(double)"), self.updateUi)
		self.setWindowTitle("Currency")
    
	# This method is called in response to thecurrentIndexChanged()signal emitted
	# by the comboboxes, and in response to thevalueChanged()signal emitted by the spinbox.
	def updateUi(self):
		to = unicode(self.toComboBox.currentText())
		from_ = unicode(self.fromComboBox.currentText())
		amount = ((self.rates[from_] / self.rates[to]) *
				self.fromSpinBox.value())
		self.toLabel.setText("%0.2f" % amount)

	def getdata(self): # Idea taken from the Python Cookbook
		self.rates = {}
		try:
			date = "Unknow"
			fh = urllib2.urlopen("http://www.bankofcanada.ca"
								"/en/markets/csv/exchange_eng.csv")
			for line in fh:
				if not line or line.startswith(("#", "Closing")):
					continue
				fields = line.split(",")
				if line.startswith("Date "):
					date = fields[-1]
				else:
					try:
						# We split each of these lines on commas and
						# take the first item to be the currency name, 
						# and the last item to be the exchange rate
						value = float(fields[-1])
						self.rates[unicode(fields[0])] = value
					except ValueError:
						pass
			# The string that is returned by getdata()is shown in the dateLabel, 
			# so normally this label will show the date applicable to the exchange rates, 
			# but in an error situation it will show the error message instead.
			return "Exchange Rates Date: " + date
		except Exception, e:
			return "Failed to download:\n%s" % e
			
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
