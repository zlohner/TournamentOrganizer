#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
import view.notifier

class ErrorMessage(QtGui.QWidget):
	def __init__(self, message, title):
		super(ErrorMessage, self).__init__()
		self.message = message

		# self.setWindowTitle(title)
		self.setStyleSheet(style.style_loader.stylesheet)

		self.label = QtGui.QLabel(str(self.message), self)

		self.label_widget = QtGui.QWidget(self)
		label_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		label_layout.addWidget(self.label)
		self.label_widget.setLayout(label_layout)

		self.submit_btn = QtGui.QPushButton('OK', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QtGui.QWidget(self)
		submit_btn_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		layout = QtGui.QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

	def submit(self):
		self.close()
