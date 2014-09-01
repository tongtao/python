# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileInfoEdit.ui'
#
# Created: Sat Aug 30 15:35:27 2014
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

class Ui_fileInfoEdit(object):
    def setupUi(self, fileInfoEdit):
        fileInfoEdit.setObjectName(_fromUtf8("fileInfoEdit"))
        fileInfoEdit.resize(349, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/pen_3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fileInfoEdit.setWindowIcon(icon)
        self.widget = QtGui.QWidget(fileInfoEdit)
        self.widget.setGeometry(QtCore.QRect(10, 10, 331, 284))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditCurPages = QtGui.QLineEdit(self.widget)
        self.lineEditCurPages.setObjectName(_fromUtf8("lineEditCurPages"))
        self.horizontalLayout.addWidget(self.lineEditCurPages)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditAllPages = QtGui.QLineEdit(self.widget)
        self.lineEditAllPages.setObjectName(_fromUtf8("lineEditAllPages"))
        self.horizontalLayout_2.addWidget(self.lineEditAllPages)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEditReadTimes = QtGui.QLineEdit(self.widget)
        self.lineEditReadTimes.setObjectName(_fromUtf8("lineEditReadTimes"))
        self.horizontalLayout_3.addWidget(self.lineEditReadTimes)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEditPro = QtGui.QLineEdit(self.widget)
        self.lineEditPro.setObjectName(_fromUtf8("lineEditPro"))
        self.horizontalLayout_4.addWidget(self.lineEditPro)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonEnt = QtGui.QPushButton(self.widget)
        self.pushButtonEnt.setObjectName(_fromUtf8("pushButtonEnt"))
        self.verticalLayout.addWidget(self.pushButtonEnt)
        self.pushButtonC = QtGui.QPushButton(self.widget)
        self.pushButtonC.setObjectName(_fromUtf8("pushButtonC"))
        self.verticalLayout.addWidget(self.pushButtonC)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.textEditModify = QtGui.QTextEdit(self.widget)
        self.textEditModify.setObjectName(_fromUtf8("textEditModify"))
        self.verticalLayout_2.addWidget(self.textEditModify)

        self.retranslateUi(fileInfoEdit)
        QtCore.QMetaObject.connectSlotsByName(fileInfoEdit)

    def retranslateUi(self, fileInfoEdit):
        fileInfoEdit.setWindowTitle(_translate("fileInfoEdit", "fileInfoEdit", None))
        self.label.setText(_translate("fileInfoEdit", "当前页数", None))
        self.label_4.setText(_translate("fileInfoEdit", "总页数", None))
        self.label_2.setText(_translate("fileInfoEdit", "遍数", None))
        self.label_5.setText(_translate("fileInfoEdit", "优先级(1-5)", None))
        self.pushButtonEnt.setText(_translate("fileInfoEdit", "确定", None))
        self.pushButtonC.setText(_translate("fileInfoEdit", "取消", None))
        self.label_3.setText(_translate("fileInfoEdit", "注释", None))

