#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QComboBox, QPushButton, QFormLayout

import style.style_loader
import view.notifier
from model.tournament_organizer import to

class RemovePlayerWidget(QWidget):
	def __init__(self):
		super(RemovePlayerWidget, self).__init__()
		# self.setWindowTitle('Remove Player')
		self.setStyleSheet(style.style_loader.stylesheet)

		self.label = QLabel('Enter Name:', self)

		self.label_widget = QWidget(self)
		label_layout = QBoxLayout(QBoxLayout.LeftToRight)
		label_layout.addWidget(self.label)
		self.label_widget.setLayout(label_layout)

		self.name_box = QComboBox(self)
		self.name_box.setFixedWidth(210)
		self.name_box.setFixedHeight(50)

		self.name_box_widget = QWidget(self)
		name_box_layout = QBoxLayout(QBoxLayout.LeftToRight)
		name_box_layout.addWidget(self.name_box)
		self.name_box_widget.setLayout(name_box_layout)

		self.submit_btn = QPushButton('Remove Player', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QWidget(self)
		submit_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		layout = QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.name_box_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

		self.show()
		self.setFixedHeight(self.height())
		self.setFixedWidth(self.width())
		self.close()

	def update(self):
		self.name_box.clear()
		for name in to.sorted_players(method='by_name'):
			self.name_box.addItem(name)

	def submit(self):
		view.notifier.player_removed(str(self.name_box.itemText(self.name_box.currentIndex())))
		self.name_box.clear()
		self.close()
