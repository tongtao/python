# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageDlg.ui'
#
# Created: Sun Aug 24 22:29:03 2014
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

class Ui_MessageDlg(object):
    def setupUi(self, MessageDlg):
        MessageDlg.setObjectName(_fromUtf8("MessageDlg"))
        MessageDlg.resize(301, 127)
        self.widget = QtGui.QWidget(MessageDlg)
        self.widget.setGeometry(QtCore.QRect(11, 20, 271, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.messagelabel = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ADMUI3Lg"))
        font.setPointSize(26)
        self.messagelabel.setFont(font)
        self.messagelabel.setTextFormat(QtCore.Qt.RichText)
        self.messagelabel.setObjectName(_fromUtf8("messagelabel"))
        self.horizontalLayout.addWidget(self.messagelabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(MessageDlg)
        QtCore.QMetaObject.connectSlotsByName(MessageDlg)

    def retranslateUi(self, MessageDlg):
        MessageDlg.setWindowTitle(_translate("MessageDlg", "Message: time is up!", None))
        self.messagelabel.setText(_translate("MessageDlg", "Time is Up!!!", None))
        self.pushButton.setText(_translate("MessageDlg", "知道啦", None))

