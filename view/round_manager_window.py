#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
from view.round_manager_widget import RoundManagerWidget

class RoundManagerWindow(QtGui.QMainWindow):
	def __init__(self):
		super(RoundManagerWindow, self).__init__()

		# self.setWindowTitle('Tournament Organizer')
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(style.style_loader.ICON_FILENAME_JPG)))
		self.setStyleSheet(style.style_loader.stylesheet)
		self.move(740, 600)

		self.round_manager_widget = RoundManagerWidget(self)
		self.setCentralWidget(self.round_manager_widget)

		self.show()
		self.setFixedWidth(self.width() + 50)
		self.setFixedHeight(self.height())
