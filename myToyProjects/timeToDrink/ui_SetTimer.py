# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetTimer.ui'
#
# Created: Mon Aug 25 09:41:51 2014
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

class Ui_SetTimerDlg(object):
    def setupUi(self, SetTimerDlg):
        SetTimerDlg.setObjectName(_fromUtf8("SetTimerDlg"))
        SetTimerDlg.resize(362, 163)
        self.widget = QtGui.QWidget(SetTimerDlg)
        self.widget.setGeometry(QtCore.QRect(10, 20, 334, 131))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 3)
        self.statuLabel = QtGui.QLabel(self.widget)
        self.statuLabel.setObjectName(_fromUtf8("statuLabel"))
        self.gridLayout.addWidget(self.statuLabel, 1, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.MessageTimeEdit = QtGui.QTimeEdit(self.widget)
        self.MessageTimeEdit.setObjectName(_fromUtf8("MessageTimeEdit"))
        self.gridLayout.addWidget(self.MessageTimeEdit, 1, 4, 1, 1)
        self.alterNumber = QtGui.QSpinBox(self.widget)
        self.alterNumber.setObjectName(_fromUtf8("alterNumber"))
        self.gridLayout.addWidget(self.alterNumber, 1, 5, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 6, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(92, 26, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonHide = QtGui.QPushButton(self.widget)
        self.pushButtonHide.setObjectName(_fromUtf8("pushButtonHide"))
        self.horizontalLayout.addWidget(self.pushButtonHide)
        self.pushButtonEnt = QtGui.QPushButton(self.widget)
        self.pushButtonEnt.setObjectName(_fromUtf8("pushButtonEnt"))
        self.horizontalLayout.addWidget(self.pushButtonEnt)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 4, 1, 3)
        self.pushButtonClear = QtGui.QPushButton(self.widget)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.gridLayout.addWidget(self.pushButtonClear, 2, 4, 1, 1)

        self.retranslateUi(SetTimerDlg)
        QtCore.QMetaObject.connectSlotsByName(SetTimerDlg)

    def retranslateUi(self, SetTimerDlg):
        SetTimerDlg.setWindowTitle(_translate("SetTimerDlg", "Dialog", None))
        self.label.setText(_translate("SetTimerDlg", "定时提醒", None))
        self.statuLabel.setText(_translate("SetTimerDlg", "Not set yet!", None))
        self.checkBox.setText(_translate("SetTimerDlg", "循环", None))
        self.pushButtonHide.setText(_translate("SetTimerDlg", "隐藏", None))
        self.pushButtonEnt.setText(_translate("SetTimerDlg", "确定", None))
        self.pushButtonClear.setText(_translate("SetTimerDlg", "清零", None))

