#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QComboBox, QSpinBox, QPushButton, QFormLayout

import style.style_loader
import view.notifier
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

MATCH_WIN_NUM_GAMES = 2

class ReportResultWidget(QWidget):
	def __init__(self):
		super(ReportResultWidget, self).__init__()
		# self.setWindowTitle('Report Result')
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

		self.record_label = QLabel('W/L/D:', self)

		self.win_box = QSpinBox(self)
		self.win_box.setMaximum(MATCH_WIN_NUM_GAMES)
		self.win_box.setMinimum(0)
		self.win_box.setSingleStep(1)
		self.win_box.setValue(0)
		self.win_box.setFixedWidth(50)
		self.win_box.setFixedHeight(50)

		self.loss_box = QSpinBox(self)
		self.loss_box.setMaximum(MATCH_WIN_NUM_GAMES)
		self.loss_box.setMinimum(0)
		self.loss_box.setSingleStep(1)
		self.loss_box.setValue(0)
		self.loss_box.setFixedWidth(50)
		self.loss_box.setFixedHeight(50)

		self.draw_box = QSpinBox(self)
		self.draw_box.setMaximum(MATCH_WIN_NUM_GAMES + 1)
		self.draw_box.setMinimum(0)
		self.draw_box.setSingleStep(1)
		self.draw_box.setValue(0)
		self.draw_box.setFixedWidth(50)
		self.draw_box.setFixedHeight(50)

		self.record_widget = QWidget(self)
		record_layout = QBoxLayout(QBoxLayout.LeftToRight)
		record_layout.addWidget(self.record_label)
		record_layout.addWidget(self.win_box)
		record_layout.addWidget(self.loss_box)
		record_layout.addWidget(self.draw_box)
		self.record_widget.setLayout(record_layout)

		self.submit_btn = QPushButton('Report Result', self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QWidget(self)
		submit_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		self.error = None

		layout = QFormLayout()
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

	def update(self):
		self.name_box.clear()
		for name in to.sorted_players(method='by_name'):
			self.name_box.addItem(name)

	def submit(self):
		try:
			record = self.get_record()
			w_l_d = self.win_loss_draw(record)
		except TournamentException as ex:
			self.error = ErrorMessage(str(ex), '')
			self.error.setStyleSheet(style.style_loader.stylesheet)
			self.error.show()

		view.notifier.report_result(str(self.name_box.itemText(self.name_box.currentIndex())), record, w_l_d)
		self.win_box.setValue(0)
		self.loss_box.setValue(0)
		self.draw_box.setValue(0)
		self.close()
