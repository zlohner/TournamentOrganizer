#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QComboBox, QPushButton, QFormLayout

import style.style_loader
import view.notifier
from model.user_manager import um

class AddPlayerWidget(QWidget):
	def __init__(self):
		super(AddPlayerWidget, self).__init__()

		self.users = {}

		# self.setWindowTitle('Add Player')
		self.setStyleSheet(style.style_loader.stylesheet)

		self.label = QLabel('Enter Name:', self)

		self.label_widget = QWidget(self)
		label_layout = QBoxLayout(QBoxLayout.LeftToRight)
		label_layout.addWidget(self.label)
		self.label_widget.setLayout(label_layout)

		self.user_box = QComboBox(self)
		self.user_box.setFixedWidth(210)
		self.user_box.setFixedHeight(50)

		self.user_box_widget = QWidget(self)
		user_box_layout = QBoxLayout(QBoxLayout.LeftToRight)
		user_box_layout.addWidget(self.user_box)
		self.user_box_widget.setLayout(user_box_layout)

		self.submit_btn = QPushButton('Add Player', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QWidget(self)
		submit_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		layout = QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.user_box_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

		self.show()
		self.setFixedHeight(self.height())
		self.setFixedWidth(self.width())
		self.close()

	def update(self):
		self.user_box.clear()
		self.users = um.users()
		for user in self.users:
			self.user_box.addItem(user.name + ' (' + str(user.id) + ')')

	def submit(self):
		user = self.users[self.user_box.currentIndex()]
		view.notifier.player_added(user.name, user)
		self.close()
