# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculateDlg.ui'
#
# Created: Sat Sep 27 17:32:21 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_calDialog(object):
    def setupUi(self, calDialog):
        calDialog.setObjectName(_fromUtf8("calDialog"))
        calDialog.resize(402, 276)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Vrinda"))
        font.setPointSize(10)
        calDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/pp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        calDialog.setWindowIcon(icon)
        self.layoutWidget = QtGui.QWidget(calDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 385, 256))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.calculateButton = QtGui.QPushButton(self.layoutWidget)
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.horizontalLayout.addWidget(self.calculateButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.proButton1 = QtGui.QPushButton(self.layoutWidget)
        self.proButton1.setObjectName(_fromUtf8("proButton1"))
        self.horizontalLayout_2.addWidget(self.proButton1)
        self.proButton2 = QtGui.QPushButton(self.layoutWidget)
        self.proButton2.setObjectName(_fromUtf8("proButton2"))
        self.horizontalLayout_2.addWidget(self.proButton2)
        self.proButton3 = QtGui.QPushButton(self.layoutWidget)
        self.proButton3.setObjectName(_fromUtf8("proButton3"))
        self.horizontalLayout_2.addWidget(self.proButton3)
        spacerItem = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)

        self.retranslateUi(calDialog)
        QtCore.QMetaObject.connectSlotsByName(calDialog)

    def retranslateUi(self, calDialog):
        calDialog.setWindowTitle(_translate("calDialog", "calculate", None))
        self.calculateButton.setText(_translate("calDialog", "calculate", None))
        self.proButton1.setText(_translate("calDialog", "proposition1", None))
        self.proButton2.setText(_translate("calDialog", "proposition2", None))
        self.proButton3.setText(_translate("calDialog", "proposition3", None))
        self.checkBox.setText(_translate("calDialog", "auto", None))

