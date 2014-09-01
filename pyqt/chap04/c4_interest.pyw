# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		
		self.principal = QDoubleSpinBox()
		self.principal.setRange(0.01, 10000000.00)
		self.principal.setPrefix("$")
		self.principal.setValue(1000)
		
		self.rate = QDoubleSpinBox()
		self.rate.setRange(0.01, 1000)
		self.rate.setSuffix("%")
		self.rate.setValue(1)
		
		self.years = QComboBox()
		yearsList = ["1 years", "2 years", "3 years", "4 years", "5 years",
						"6 years", "7 years", "8 years", "9 years", "10 years"]
		self.years.addItems(yearsList)
		
		self.amounts = QLabel("$%d" % (1000 * ((1 + (1 / 100.0)) ** 1)))
		
		priLab = QLabel("Principal:")
		ratLab = QLabel("Rate:")
		yearLab = QLabel("Years:")
		amnLab = QLabel("Amount")
		
		grid = QGridLayout()
		grid.addWidget(priLab, 0, 0)
		grid.addWidget(self.principal, 0, 1)
		grid.addWidget(ratLab, 1, 0)
		grid.addWidget(self.rate, 1, 1)
		grid.addWidget(yearLab, 2, 0)
		grid.addWidget(self.years, 2, 1)
		grid.addWidget(amnLab, 3, 0)
		grid.addWidget(self.amounts, 3, 1)
		self.setLayout(grid)
		
		self.setWindowTitle("interest")
		
		self.connect(self.principal,
				SIGNAL("valueChanged(double)"), self.updateUi)
		self.connect(self.rate,
				SIGNAL("valueChanged(double)"), self.updateUi)		
		self.connect(self.years,
				SIGNAL("currentIndexChanged(int)"), self.updateUi)
				
	def updateUi(self):
		n_years = self.years.currentIndex() + 1
		n_amounts = (self.principal.value() * (( 1 + (self.rate.value() / 100.0)) ** n_years))
					
		self.amounts.setText("$%.2f" % n_amounts)
				
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()	