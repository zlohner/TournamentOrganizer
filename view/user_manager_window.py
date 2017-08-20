#!/usr/bin/env python3

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QMainWindow

import style.style_loader
from view.user_manager_widget import UserManagerWidget

class UserManagerWindow(QMainWindow):
	def __init__(self):
		super(UserManagerWindow, self).__init__()

		self.setWindowIcon(QIcon(QPixmap(style.style_loader.ICON_FILENAME_JPG)))
		self.setStyleSheet(style.style_loader.stylesheet)

		self.user_manager_widget = UserManagerWidget(self)
		self.setCentralWidget(self.user_manager_widget)
		self.move(100, 200)

		self.show()
		self.setFixedWidth(self.width())
		self.setFixedHeight(self.height())

	def show_add_user_widget(self):
		# TODO: implement add user widget
		pass

	def show_remove_user_widget(self):
		# TODO: implement remove user widget
		pass
