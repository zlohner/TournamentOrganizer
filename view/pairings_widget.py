#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QFormLayout

import style.style_loader
import view.notifier
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

class PairingsWidget(QWidget):
	def __init__(self, parent):
		super(PairingsWidget, self).__init__(parent)
		self.parent = parent

		view.notifier.observers.append(self)

		self.header_label = QLabel('Pairings')

		self.header_widget = QWidget(self)
		header_layout = QBoxLayout(QBoxLayout.TopToBottom)
		header_layout.addWidget(self.header_label)
		self.header_widget.setLayout(header_layout)

		self.pairings_list = QTableWidget(style.style_loader.TABLE_INITIAL_LENGTH, 2, self)
		self.pairings_list.setFixedHeight(300)
		self.pairings_list.setFixedWidth(400)
		self.pairings_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.pairings_list.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

		self.pairings_list_widget = QWidget(self)
		pairings_list_layout = QBoxLayout(QBoxLayout.LeftToRight)
		pairings_list_layout.addWidget(self.pairings_list)
		self.pairings_list_widget.setLayout(pairings_list_layout)

		self.report_btn = QPushButton('Report Results', self)
		self.report_btn.clicked.connect(parent.show_report_result_widget)

		self.report_btn_widget = QWidget(self)
		report_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		report_btn_layout.addWidget(self.report_btn)
		self.report_btn_widget.setLayout(report_btn_layout)

		layout = QFormLayout()
		layout.addRow(self.header_widget)
		layout.addRow(self.pairings_list_widget)
		layout.addRow(self.report_btn_widget)
		self.setLayout(layout)

		self.update()

	def update(self):
		self.pairings_list.clearContents()

		index = 0
		for p1, p2 in to.pairings.items():
			if index == self.pairings_list.rowCount():
				self.pairings_list.insertRow(index)
			p1_item = QTableWidgetItem(p1)
			p1_item.setFlags(p1_item.flags() & ~Qt.ItemIsEditable)
			self.pairings_list.setItem(index, 0, p1_item)
			if p2 == None:
				p2_str = '--BYE--'
			else:
				p2_str = p2
			p2_item = QTableWidgetItem(p2_str)
			p2_item.setFlags(p2_item.flags() & ~Qt.ItemIsEditable)
			self.pairings_list.setItem(index, 1, p2_item)
			index += 1
		self.pairings_list.show()

	def player_added(self, player, user):
		pass

	def player_removed(self, player):
		pass

	def pairings_created(self):
		self.update()
		self.parent.show()

	def report_result(self, player, record, win_loss_draw):
		try:
			if win_loss_draw == 'win':
				to.record_win(player, record)
			elif win_loss_draw == 'loss':
				to.record_loss(player, record)
			elif win_loss_draw == 'draw':
				to.record_draw(player, record)
			view.notifier.result_reported()
		except TournamentException as ex:
			self.error = ErrorMessage(str(ex), '')
			self.error.setStyleSheet(style.style_loader.stylesheet)
			self.error.show()

	def result_reported(self):
		self.update()
		self.parent.show()

	def reset(self):
		self.update()
		self.parent.show()
