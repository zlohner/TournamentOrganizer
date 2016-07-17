#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
import view.notifier
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

MATCH_WIN_NUM_GAMES = 2

class ReportResultWidget(QtGui.QWidget):
	def __init__(self):
		super(ReportResultWidget, self).__init__()
		# self.setWindowTitle('Report Result')
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

		self.record_label = QtGui.QLabel('W/L/D:', self)

		self.win_box = QtGui.QSpinBox(self)
		self.win_box.setMaximum(MATCH_WIN_NUM_GAMES)
		self.win_box.setMinimum(0)
		self.win_box.setSingleStep(1)
		self.win_box.setValue(0)
		self.win_box.setFixedWidth(50)
		self.win_box.setFixedHeight(50)

		self.loss_box = QtGui.QSpinBox(self)
		self.loss_box.setMaximum(MATCH_WIN_NUM_GAMES)
		self.loss_box.setMinimum(0)
		self.loss_box.setSingleStep(1)
		self.loss_box.setValue(0)
		self.loss_box.setFixedWidth(50)
		self.loss_box.setFixedHeight(50)

		self.draw_box = QtGui.QSpinBox(self)
		self.draw_box.setMaximum(MATCH_WIN_NUM_GAMES + 1)
		self.draw_box.setMinimum(0)
		self.draw_box.setSingleStep(1)
		self.draw_box.setValue(0)
		self.draw_box.setFixedWidth(50)
		self.draw_box.setFixedHeight(50)

		self.record_widget = QtGui.QWidget(self)
		record_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		record_layout.addWidget(self.record_label)
		record_layout.addWidget(self.win_box)
		record_layout.addWidget(self.loss_box)
		record_layout.addWidget(self.draw_box)
		self.record_widget.setLayout(record_layout)

		self.submit_btn = QtGui.QPushButton('Report Result', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QtGui.QWidget(self)
		submit_btn_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		self.error = None

		layout = QtGui.QFormLayout()
		layout.addRow(self.label_widget)
		layout.addRow(self.name_box_widget)
		layout.addRow(self.record_widget)
		layout.addRow(self.submit_btn_widget)
		self.setLayout(layout)

		self.show()
		self.setFixedHeight(self.height())
		self.setFixedWidth(self.width())
		self.close()

	def get_record(self):
		return (self.win_box.value(), self.loss_box.value(), self.draw_box.value())

	def win_loss_draw(self, record):
		w, l, d = record
		if w > l:
			return 'win'
		elif w < l:
			return 'loss'
		else:
			return 'draw'

	def submit(self):
		try:
			record = self.get_record()
			w_l_d = self.win_loss_draw(record)
		except TournamentException as ex:
			self.error = ErrorMessage(str(ex), '')
			self.error.setStyleSheet(style.style_loader.stylesheet)
			self.error.show()

		view.notifier.report_result(str(self.name_box.text()), record, w_l_d)
		self.name_box.clear()
		self.win_box.setValue(0)
		self.loss_box.setValue(0)
		self.draw_box.setValue(0)
		self.close()
