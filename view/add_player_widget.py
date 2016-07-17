#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
import view.notifier

class AddPlayerWidget(QtGui.QWidget):
	def __init__(self):
		super(AddPlayerWidget, self).__init__()
		# self.setWindowTitle('Add Player')
		self.setStyleSheet(style.style_loader.stylesheet)

		self.label = QtGui.QLabel('Enter Name:', self)

		self.label_widget = QtGui.QWidget(self)
		label_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		label_layout.addWidget(self.label)
		self.label_widget.setLayout(label_layout)

		self.name_box = QtGui.QLineEdit(self)
		self.name_box.setFixedWidth(210)
		self.name_box.setFixedHeight(50)

		self.name_box_widget = QtGui.QWidget(self)
		name_box_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		name_box_layout.addWidget(self.name_box)
		self.name_box_widget.setLayout(name_box_layout)

		self.submit_btn = QtGui.QPushButton('Add Player', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QtGui.QWidget(self)
		submit_btn_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		layout = QtGui.QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.name_box_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

		self.show()
		self.setFixedHeight(self.height())
		self.setFixedWidth(self.width())
		self.close()

	def submit(self):
		view.notifier.player_added(str(self.name_box.text()))
		self.name_box.clear()
		self.close()
