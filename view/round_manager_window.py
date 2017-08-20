#!/usr/bin/env python3

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow

import style.style_loader
from view.round_manager_widget import RoundManagerWidget

class RoundManagerWindow(QMainWindow):
	def __init__(self):
		super(RoundManagerWindow, self).__init__()

		# self.setWindowTitle('Tournament Organizer')
		self.setWindowIcon(QIcon(QPixmap(style.style_loader.ICON_FILENAME_JPG)))
		self.setStyleSheet(style.style_loader.stylesheet)
		self.move(1150, 720)

		self.round_manager_widget = RoundManagerWidget(self)
		self.setCentralWidget(self.round_manager_widget)

		self.show()
		self.setFixedWidth(self.width() + 50)
		self.setFixedHeight(self.height())
