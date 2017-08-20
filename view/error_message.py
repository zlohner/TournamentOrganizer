#!/usr/bin/env python3

from PyQt5.QtWidgets import QLabel, QWidget, QBoxLayout, QPushButton, QFormLayout

import style.style_loader
import view.notifier

class ErrorMessage(QWidget):
	def __init__(self, message, title):
		super(ErrorMessage, self).__init__()
		self.message = message

		# self.setWindowTitle(title)
		self.setStyleSheet(style.style_loader.stylesheet)

		self.label = QLabel(str(self.message), self)

		self.label_widget = QWidget(self)
		label_layout = QBoxLayout(QBoxLayout.LeftToRight)
		label_layout.addWidget(self.label)
		self.label_widget.setLayout(label_layout)

		self.submit_btn = QPushButton('OK', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QWidget(self)
		submit_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		layout = QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

		self.show()
		self.setFixedHeight(self.height())
		self.setFixedWidth(self.width())
		self.close()

	def submit(self):
		self.close()
