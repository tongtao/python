# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import*

import ui_calculateDlg
import logicPropositon

sys.stderr = open("errlog.txt", "w")

class calProDlg(QDialog, 
                ui_calculateDlg.Ui_calDialog):
    def __init__(self, parent=None):
        super(calProDlg, self).__init__(parent)
        
        self.setupUi(self)
        
        self.initUi()
        
        self.autoFlag = False
        
        self.proButton1.clicked.connect(self.printTablePor1)
        self.proButton2.clicked.connect(self.printTablePor2)
        self.proButton3.clicked.connect(self.printTablePor3)
    
    def on_checkBox_stateChanged(self):
        self.autoFlag = self.checkBox.isChecked()
        
        
    @pyqtSignature("QString")
    def on_lineEdit_textChanged(self):
        if self.autoFlag:
            self.calculateButton.setEnabled(True)
            userProStr = self.lineEdit.text()
            printTableStr = logicPropositon.printTableStr(userProStr)
            self.printTable(printTableStr)
        else:
            self.calculateButton.setEnabled(True)
            
    def on_calculateButton_clicked(self):
        userProStr = self.lineEdit.text()
        printTableStr = logicPropositon.printTableStr(userProStr)
        self.printTable(printTableStr)
        
    def printTablePor1(self):
        printTableStr = logicPropositon.printTableStr(logicPropositon.propositionList[0])
        self.printTable(printTableStr)
    
    def printTablePor2(self):
        printTableStr = logicPropositon.printTableStr(logicPropositon.propositionList[1])
        self.printTable(printTableStr)
    
    def printTablePor3(self):
        printTableStr = logicPropositon.printTableStr(logicPropositon.propositionList[2])
        self.printTable(printTableStr)
        
        
    def printTable(self, tableStr): 
        self.textEdit.clear()
        self.textEdit.setText(tableStr)
        
    def initUi(self):
        self.calculateButton.setEnabled(False)
        self.textEdit.setReadOnly(True)
        #self.textEdit.setText(logicPropositon.readMe)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    form = calProDlg()
    form.show()
    
    form.exec_()