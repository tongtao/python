# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookManagerWindow.ui'
#
# Created: Sat Aug 30 14:38:43 2014
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

class Ui_bookManager(object):
    def setupUi(self, bookManager):
        bookManager.setObjectName(_fromUtf8("bookManager"))
        bookManager.resize(515, 537)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bookManager.sizePolicy().hasHeightForWidth())
        bookManager.setSizePolicy(sizePolicy)
        bookManager.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/layers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bookManager.setWindowIcon(icon)
        self.bookTree = QtGui.QTreeWidget(bookManager)
        self.bookTree.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookTree.sizePolicy().hasHeightForWidth())
        self.bookTree.setSizePolicy(sizePolicy)
        self.bookTree.setMinimumSize(QtCore.QSize(1, 0))
        self.bookTree.setBaseSize(QtCore.QSize(300, 300))
        self.bookTree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bookTree.setAutoFillBackground(True)
        self.bookTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.bookTree.setAllColumnsShowFocus(False)
        self.bookTree.setObjectName(_fromUtf8("bookTree"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.bookTree)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bookTree.header().setCascadingSectionResizes(True)
        self.bookTree.header().setDefaultSectionSize(199)
        self.bookTree.header().setMinimumSectionSize(0)
        self.bookTree.header().setSortIndicatorShown(True)
        self.toolBar = QtGui.QToolBar(bookManager)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        bookManager.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        bookManager.insertToolBarBreak(self.toolBar)
        self.actionSelectDir = QtGui.QAction(bookManager)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectDir.setIcon(icon1)
        self.actionSelectDir.setObjectName(_fromUtf8("actionSelectDir"))
        self.actionOpenFile = QtGui.QAction(bookManager)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/book_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon2)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionSyncTree = QtGui.QAction(bookManager)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/cloud_upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSyncTree.setIcon(icon3)
        self.actionSyncTree.setObjectName(_fromUtf8("actionSyncTree"))
        self.actionEdit = QtGui.QAction(bookManager)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/pen_3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon4)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionFind = QtGui.QAction(bookManager)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/magnifying_glass.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon5)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.toolBar.addAction(self.actionSelectDir)
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionSyncTree)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionFind)

        self.retranslateUi(bookManager)
        QtCore.QMetaObject.connectSlotsByName(bookManager)

    def retranslateUi(self, bookManager):
        bookManager.setWindowTitle(_translate("bookManager", "BookManager", None))
        self.bookTree.headerItem().setText(0, _translate("bookManager", "书名", None))
        self.bookTree.headerItem().setText(1, _translate("bookManager", "进度", None))
        self.bookTree.headerItem().setText(2, _translate("bookManager", "时间", None))
        self.toolBar.setWindowTitle(_translate("bookManager", "toolBar", None))
        self.actionSelectDir.setText(_translate("bookManager", "选择所在文件夹", None))
        self.actionOpenFile.setText(_translate("bookManager", "打开文件", None))
        self.actionSyncTree.setText(_translate("bookManager", "更新", None))
        self.actionEdit.setText(_translate("bookManager", "编辑信息", None))
        self.actionFind.setText(_translate("bookManager", "查找文件", None))

