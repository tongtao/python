# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

# Python’s standard modules
import os
import platform
import sys
# third party modules
from PyQt4.QtCore import (PYQT_VERSION_STR, QFile, QFileInfo, QSettings,
		QString, QT_VERSION_STR, QTimer, QVariant, Qt, SIGNAL)
from PyQt4.QtGui import (QAction, QActionGroup, QApplication,
		QDockWidget, QFileDialog, QFrame, QIcon, QImage, QImageReader,
		QImageWriter, QInputDialog, QKeySequence, QLabel, QListWidget,
		QMainWindow, QMessageBox, QPainter, QPixmap, QPrintDialog,
		QPrinter, QSpinBox)
# our own modules
import helpform
import newimagedlg
import qrc_resources  # # pyrcc4 -o qrc_resources.py resources.qrc

# __version__ will be used it in the application’s about box
__version__ = "1.0.0"


class MainWindow(QMainWindow):

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		
		# a null QImagethat we will use to hold the image the user loads or creates
		self.image = QImage()
		# dirty as a Boolean flag to indicate whether the image has unsaved changes
		self.dirty = False
		# filename is initially set to Non
		self.filename = None
		# mirroring capabilities
		# keep track of the mirrored state 
		self.mirroredvertically = False
		self.mirroredhorizontally = False

		##### Central Widget #####
		# A QLabel can display plain text, or HTML, 
		# or an image in any of the image formats that PyQt supports
		self.imageLabel = QLabel()
		# set a minimum size because initially the label has nothing to show, and would therefore take up no space
		self.imageLabel.setMinimumSize(200, 200)
		# align our images vertically and horizontally centered
		self.imageLabel.setAlignment(Qt.AlignCenter)
		# creating context menus
		# First, we must set the context menu policy for the widget which we want to have a context menu.
		self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
		# in a main-window-style application we only ever have one central widget
		# This method both lays out the widget in the main window’s central area,
		# and reparents the widget so that the main window takes ownership of it.
		self.setCentralWidget(self.imageLabel)

		##### Dock Widget #####
		# We can add a single widget to a dock widget, just as we can have a single widget in a main window’s central area
		# in addition to providing their window caption, we must give them a parent
		logDockWidget = QDockWidget("Log", self)
		# set an object name here because we want PyQt to save and restore the dock widget’s size and position
		logDockWidget.setObjectName("LogDockWidget")
		logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|
									  Qt.RightDockWidgetArea)
		self.listWidget = QListWidget()
		logDockWidget.setWidget(self.listWidget)
		self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

		self.printer = None

		# creating a QLabelwidget and adding it to the status bar
		self.sizeLabel = QLabel()
		# QFrame.StyledPanel	0x0006	draws a rectangular panel with a look that depends on the current GUI style. It can be raised or sunken.
		# QFrame.Sunken	0x0030	the frame and contents appear sunken; draws a 3D sunken line using the light and dark colors of the current color group
		self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
		status = self.statusBar()
		# switch off the status bar’s size grip since that seems inappropriate 
		# when we have an indicator label that shows the image’s dimensions
		status.setSizeGripEnabled(False)
		status.addPermanentWidget(self.sizeLabel)
		# the second argument is the number of milliseconds (5 000, i.e., 5 seconds), 
		# that the message should be shown for; after this time the status bar will clear itself.
		status.showMessage("Ready", 5000)

		##### Actions #####
		fileNewAction = self.createAction("&New...", self.fileNew,
				QKeySequence.New, "filenew", "Create an image file")
		fileOpenAction = self.createAction("&Open...", self.fileOpen,
				QKeySequence.Open, "fileopen",
				"Open an existing image file")
		fileSaveAction = self.createAction("&Save", self.fileSave,
				QKeySequence.Save, "filesave", "Save the image")
		fileSaveAsAction = self.createAction("Save &As...",
				self.fileSaveAs, icon="filesaveas",
				tip="Save the image using a new name")
		filePrintAction = self.createAction("&Print", self.filePrint,
				QKeySequence.Print, "fileprint", "Print the image")
		fileQuitAction = self.createAction("&Quit", self.close,
				"Ctrl+Q", "filequit", "Close the application")
		editInvertAction = self.createAction("&Invert",
				self.editInvert, "Ctrl+I", "editinvert",
				"Invert the image's colors", True, "toggled(bool)")
		editSwapRedAndBlueAction = self.createAction("Sw&ap Red and Blue",
				self.editSwapRedAndBlue, "Ctrl+A", "editswap",
				"Swap the image's red and blue color components", True,
				"toggled(bool)")
		editZoomAction = self.createAction("&Zoom...", self.editZoom,
				"Alt+Z", "editzoom", "Zoom the image")
				
		##### mirrorGroup Actions #####	
		# An action group is a class which manages a set of checkable actions and ensures that 
		# if one of the actions it manages is set to “on”, the others are all set to “off ”.
		mirrorGroup = QActionGroup(self)
		editUnMirrorAction = self.createAction("&Unmirror",
				self.editUnMirror, "Ctrl+U", "editunmirror",
				"Unmirror the image", True, "toggled(bool)")
		mirrorGroup.addAction(editUnMirrorAction)
		editMirrorHorizontalAction = self.createAction(
				"Mirror &Horizontally", self.editMirrorHorizontal,
				"Ctrl+H", "editmirrorhoriz",
				"Horizontally mirror the image", True, "toggled(bool)")
		mirrorGroup.addAction(editMirrorHorizontalAction)
		editMirrorVerticalAction = self.createAction(
				"Mirror &Vertically", self.editMirrorVertical,
				"Ctrl+V", "editmirrorvert",
				"Vertically mirror the image", True, "toggled(bool)")
		mirrorGroup.addAction(editMirrorVerticalAction)
		# Checkable actions default to being “off ”, but when we have a group like this
		# where exactly one must be “on” at a time, we must choose one to be on in the
		# first place.
		editUnMirrorAction.setChecked(True)
		
		helpAboutAction = self.createAction("&About Image Changer",
				self.helpAbout)
		helpHelpAction = self.createAction("&Help", self.helpHelp,
				QKeySequence.HelpContents)

		##### Menus #####
		# the create and populate of File menu is different from most other menus such as Edit menu, Help menu
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenuActions = (fileNewAction, fileOpenAction,
				fileSaveAction, fileSaveAsAction, None, filePrintAction,
				fileQuitAction)
		# The connection ensures that whenever the Filemenu is invoked our updateFileMenu() slot will be called.
		self.connect(self.fileMenu, SIGNAL("aboutToShow()"),
					 self.updateFileMenu)
					 
		# created the Edit menu, and then used addActions()to add some actions to it. 
		editMenu = self.menuBar().addMenu("&Edit")
		self.addActions(editMenu, (editInvertAction,
				editSwapRedAndBlueAction, editZoomAction))
		# Submenus are added to their parent menu usingQMenu.addMenu()
		mirrorMenu = editMenu.addMenu(QIcon(":/editmirror.png"),
									  "&Mirror")
		self.addActions(mirrorMenu, (editUnMirrorAction,
				editMirrorHorizontalAction, editMirrorVerticalAction))
		helpMenu = self.menuBar().addMenu("&Help")
		self.addActions(helpMenu, (helpAboutAction, helpHelpAction))

		##### Toolbars #####
		# calladdToolBar()to create a QToolBar object and populate it using addActions()
		# set an object name so that PyQt can save and restore the toolbar’s position
		# there can be any number of toolbars and PyQt uses the object name to distinguish between them
		fileToolbar = self.addToolBar("File")
		fileToolbar.setObjectName("FileToolBar")
		self.addActions(fileToolbar, (fileNewAction, fileOpenAction,
									  fileSaveAsAction))
									  
		editToolbar = self.addToolBar("Edit")
		editToolbar.setObjectName("EditToolBar")
		self.addActions(editToolbar, (editInvertAction,
				editSwapRedAndBlueAction, editUnMirrorAction,
				editMirrorVerticalAction, editMirrorHorizontalAction))
		# The pattern for adding widgets to a toolbar is always the same
		self.zoomSpinBox = QSpinBox()
		self.zoomSpinBox.setRange(1, 400)
		self.zoomSpinBox.setSuffix(" %")
		self.zoomSpinBox.setValue(100)
		self.zoomSpinBox.setToolTip("Zoom the image")
		self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
		self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
		self.connect(self.zoomSpinBox,
					 SIGNAL("valueChanged(int)"), self.showImage)
		editToolbar.addWidget(self.zoomSpinBox)

		##### context menu #####
		self.addActions(self.imageLabel, (editInvertAction,
				editSwapRedAndBlueAction, editUnMirrorAction,
				editMirrorVerticalAction, editMirrorHorizontalAction))

		self.resetableActions = ((editInvertAction, False),
								 (editSwapRedAndBlueAction, False),
								 (editUnMirrorAction, True))

		settings = QSettings()
		self.recentFiles = settings.value("RecentFiles").toStringList()
		self.restoreGeometry(
				settings.value("MainWindow/Geometry").toByteArray())
		self.restoreState(settings.value("MainWindow/State").toByteArray())
		
		self.setWindowTitle("Image Changer")
		self.updateFileMenu()
		QTimer.singleShot(0, self.loadInitialFile)


	def createAction(self, text, slot=None, shortcut=None, icon=None,
					 tip=None, checkable=False, signal="triggered()"):
		action = QAction(text, self)
		if icon is not None:
			action.setIcon(QIcon(":/{0}.png".format(icon)))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
			self.connect(action, SIGNAL(signal), slot)
		if checkable:
			action.setCheckable(True)
		return action
		
		

	#fileNewAction = self.createAction("&New...", self.fileNew,
			 #QKeySequence.New, "filenew", "Create an image file")
		#self = self
		#text = "&New..."
		#slot = self.fileNew
		#shortcut = QKeySequence.New  #QKeySequence class provides constants for the
				#standardized key sequences, such as QKeySequence.New  or use a string setShortcut("Ctrl+Q")
		#icon = "filenew"  # 
		#tip = "Create an image file"
		#checkable  # An action is checkable if it can have “on” and “off ”
		
	#fileQuitAction = self.createAction("&Quit", self.close,
		#"Ctrl+Q", "filequit", "Close the application")



	def addActions(self, target, actions):
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addAction(action)


	def closeEvent(self, event):
		if self.okToContinue():
			settings = QSettings()
			filename = (QVariant(QString(self.filename))
						if self.filename is not None else QVariant())
			settings.setValue("LastFile", filename)
			recentFiles = (QVariant(self.recentFiles)
						   if self.recentFiles else QVariant())
			settings.setValue("RecentFiles", recentFiles)
			settings.setValue("MainWindow/Geometry", QVariant(
							  self.saveGeometry()))
			settings.setValue("MainWindow/State", QVariant(
							  self.saveState()))
		else:
			event.ignore()


	def okToContinue(self):
		if self.dirty:
			reply = QMessageBox.question(self,
					"Image Changer - Unsaved Changes",
					"Save unsaved changes?",
					QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if reply == QMessageBox.Cancel:
				return False
			elif reply == QMessageBox.Yes:
				return self.fileSave()
		return True


	def loadInitialFile(self):
		settings = QSettings()
		fname = unicode(settings.value("LastFile").toString())
		if fname and QFile.exists(fname):
			self.loadFile(fname)


	def updateStatus(self, message):
		self.statusBar().showMessage(message, 5000)
		self.listWidget.addItem(message)
		if self.filename is not None:
			self.setWindowTitle("Image Changer - {0}[*]".format(
								os.path.basename(self.filename)))
		elif not self.image.isNull():
			self.setWindowTitle("Image Changer - Unnamed[*]")
		else:
			self.setWindowTitle("Image Changer[*]")
		self.setWindowModified(self.dirty)


	def updateFileMenu(self):
		self.fileMenu.clear()
		self.addActions(self.fileMenu, self.fileMenuActions[:-1])
		current = (QString(self.filename)
				   if self.filename is not None else None)
		recentFiles = []
		for fname in self.recentFiles:
			if fname != current and QFile.exists(fname):
				recentFiles.append(fname)
		if recentFiles:
			self.fileMenu.addSeparator()
			for i, fname in enumerate(recentFiles):
				action = QAction(QIcon(":/icon.png"),
						"&{0} {1}".format(i + 1, QFileInfo(
						fname).fileName()), self)
				action.setData(QVariant(fname))
				self.connect(action, SIGNAL("triggered()"),
							 self.loadFile)
				self.fileMenu.addAction(action)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.fileMenuActions[-1])


	def fileNew(self):
		if not self.okToContinue():
			return
		dialog = newimagedlg.NewImageDlg(self)
		if dialog.exec_():
			self.addRecentFile(self.filename)
			self.image = QImage()
			for action, check in self.resetableActions:
				action.setChecked(check)
			self.image = dialog.image()
			self.filename = None
			self.dirty = True
			self.showImage()
			self.sizeLabel.setText("{0} x {1}".format(self.image.width(),
													  self.image.height()))
			self.updateStatus("Created new image")


	def fileOpen(self):
		if not self.okToContinue():
			return
		dir = (os.path.dirname(self.filename)
			   if self.filename is not None else ".")
		formats = (["*.{0}".format(unicode(format).lower())
				for format in QImageReader.supportedImageFormats()])
		fname = unicode(QFileDialog.getOpenFileName(self,
				"Image Changer - Choose Image", dir,
				"Image files ({0})".format(" ".join(formats))))
		if fname:
			self.loadFile(fname)


	def loadFile(self, fname=None):
		if fname is None:
			action = self.sender()
			if isinstance(action, QAction):
				fname = unicode(action.data().toString())
				if not self.okToContinue():
					return
			else:
				return
		if fname:
			self.filename = None
			image = QImage(fname)
			if image.isNull():
				message = "Failed to read {0}".format(fname)
			else:
				self.addRecentFile(fname)
				self.image = QImage()
				for action, check in self.resetableActions:
					action.setChecked(check)
				self.image = image
				self.filename = fname
				self.showImage()
				self.dirty = False
				self.sizeLabel.setText("{0} x {1}".format(
									   image.width(), image.height()))
				message = "Loaded {0}".format(os.path.basename(fname))
			self.updateStatus(message)


	def addRecentFile(self, fname):
		if fname is None:
			return
		if not self.recentFiles.contains(fname):
			self.recentFiles.prepend(QString(fname))
			while self.recentFiles.count() > 9:
				self.recentFiles.takeLast()


	def fileSave(self):
		if self.image.isNull():
			return True
		if self.filename is None:
			return self.fileSaveAs()
		else:
			if self.image.save(self.filename, None):
				self.updateStatus("Saved as {0}".format(self.filename))
				self.dirty = False
				return True
			else:
				self.updateStatus("Failed to save {0}".format(
								  self.filename))
				return False


	def fileSaveAs(self):
		if self.image.isNull():
			return True
		fname = self.filename if self.filename is not None else "."
		formats = (["*.{0}".format(unicode(format).lower())
				for format in QImageWriter.supportedImageFormats()])
		fname = unicode(QFileDialog.getSaveFileName(self,
				"Image Changer - Save Image", fname,
				"Image files ({0})".format(" ".join(formats))))
		if fname:
			if "." not in fname:
				fname += ".png"
			self.addRecentFile(fname)
			self.filename = fname
			return self.fileSave()
		return False


	def filePrint(self):
		if self.image.isNull():
			return
		if self.printer is None:
			self.printer = QPrinter(QPrinter.HighResolution)
			self.printer.setPageSize(QPrinter.Letter)
		form = QPrintDialog(self.printer, self)
		if form.exec_():
			painter = QPainter(self.printer)
			rect = painter.viewport()
			size = self.image.size()
			size.scale(rect.size(), Qt.KeepAspectRatio)
			painter.setViewport(rect.x(), rect.y(), size.width(),
								size.height())
			painter.drawImage(0, 0, self.image)


	def editInvert(self, on):
		if self.image.isNull():
			return
		self.image.invertPixels()
		self.showImage()
		self.dirty = True
		self.updateStatus("Inverted" if on else "Uninverted")


	def editSwapRedAndBlue(self, on):
		if self.image.isNull():
			return
		self.image = self.image.rgbSwapped()
		self.showImage()
		self.dirty = True
		self.updateStatus(("Swapped Red and Blue"
						   if on else "Unswapped Red and Blue"))


	def editUnMirror(self, on):
		if self.image.isNull():
			return
		if self.mirroredhorizontally:
			self.editMirrorHorizontal(False)
		if self.mirroredvertically:
			self.editMirrorVertical(False)


	def editMirrorHorizontal(self, on):
		if self.image.isNull():
			return
		self.image = self.image.mirrored(True, False)
		self.showImage()
		self.mirroredhorizontally = not self.mirroredhorizontally
		self.dirty = True
		self.updateStatus(("Mirrored Horizontally"
						   if on else "Unmirrored Horizontally"))


	def editMirrorVertical(self, on):
		if self.image.isNull():
			return
		self.image = self.image.mirrored(False, True)
		self.showImage()
		self.mirroredvertically = not self.mirroredvertically
		self.dirty = True
		self.updateStatus(("Mirrored Vertically"
						   if on else "Unmirrored Vertically"))


	def editZoom(self):
		if self.image.isNull():
			return
		percent, ok = QInputDialog.getInteger(self,
				"Image Changer - Zoom", "Percent:",
				self.zoomSpinBox.value(), 1, 400)
		if ok:
			self.zoomSpinBox.setValue(percent)


	def showImage(self, percent=None):
		if self.image.isNull():
			return
		if percent is None:
			percent = self.zoomSpinBox.value()
		factor = percent / 100.0
		width = self.image.width() * factor
		height = self.image.height() * factor
		image = self.image.scaled(width, height, Qt.KeepAspectRatio)
		self.imageLabel.setPixmap(QPixmap.fromImage(image))


	def helpAbout(self):
		QMessageBox.about(self, "About Image Changer",
				"""<b>Image Changer</b> v {0}
				<p>Copyright &copy; 2008 Qtrac Ltd. 
				All rights reserved.
				<p>This application can be used to perform
				simple image manipulations.
				<p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
				__version__, platform.python_version(),
				QT_VERSION_STR, PYQT_VERSION_STR,
				platform.system()))


	def helpHelp(self):
		form = helpform.HelpForm("index.html", self)
		form.show()


def main():
	app = QApplication(sys.argv)
	
	app.setOrganizationName("Qtrac Ltd.")
	app.setOrganizationDomain("qtrac.eu")
	app.setApplicationName("Image Changer")
	
	app.setWindowIcon(QIcon(":/icon.png"))
	
	form = MainWindow()
	form.show()
	app.exec_()


main()

