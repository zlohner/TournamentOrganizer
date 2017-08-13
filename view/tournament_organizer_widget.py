#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout

import style.style_loader
import view.notifier
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

class TournamentOrganizerWidget(QWidget):
	def __init__(self, parent):
		super(TournamentOrganizerWidget, self).__init__(parent)
		self.parent = parent

		# Default Players (for quick testing)
		player_names = [
			'Frodo',
			'Sam',
			'Merry',
			'Pippin',
			'Gandalf',
			'Aragorn',
			'Legolas',
			'Gimli',
			'Boromir'
		]
		# for name in player_names:
		# 	to.add_player(name)

		self.sort_order = 'by_name'

		view.notifier.observers.append(self)

		self.header_label = QLabel('Players')

		self.header_widget = QWidget(self)
		header_layout = QBoxLayout(QBoxLayout.LeftToRight)
		header_layout.addWidget(self.header_label)
		self.header_widget.setLayout(header_layout)

		self.sort_by_name_btn = QPushButton('Sort by Name', self)
		self.sort_by_name_btn.clicked.connect(self.sort_by_name)
		self.sort_by_rank_btn = QPushButton('Sort by Rank', self)
		self.sort_by_rank_btn.clicked.connect(self.sort_by_rank)

		self.sort_btns_widget = QWidget(self)
		sort_btns_layout = QBoxLayout(QBoxLayout.LeftToRight)
		sort_btns_layout.addWidget(self.sort_by_name_btn)
		sort_btns_layout.addSpacing(10)
		sort_btns_layout.addWidget(self.sort_by_rank_btn)
		self.sort_btns_widget.setLayout(sort_btns_layout)

		self.player_list = QTableWidget(style.style_loader.TABLE_INITIAL_LENGTH, 2, self)
		self.player_list.setFixedHeight(300)
		self.player_list.setFixedWidth(400)
		# self.player_list.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		# self.player_list.verticalHeader().setResizeMode(QHeaderView.Fixed)

		self.player_list_widget = QWidget(self)
		player_list_layout = QBoxLayout(QBoxLayout.LeftToRight)
		player_list_layout.addWidget(self.player_list)
		self.player_list_widget.setLayout(player_list_layout)

		self.add_player_btn = QPushButton('Add Player', self)
		self.add_player_btn.clicked.connect(self.parent.show_add_player_widget)
		self.remove_player_btn = QPushButton('Remove Player', self)
		self.remove_player_btn.clicked.connect(self.parent.show_remove_player_widget)

		self.player_btns_widget = QWidget(self)
		player_btn_layout = QBoxLayout(QBoxLayout.LeftToRight)
		player_btn_layout.addWidget(self.add_player_btn)
		player_btn_layout.addSpacing(10)
		player_btn_layout.addWidget(self.remove_player_btn)
		self.player_btns_widget.setLayout(player_btn_layout)

		self.error = None

		layout = QFormLayout()
		layout.addRow(self.header_widget)
		layout.addRow(self.sort_btns_widget)
		layout.addRow(self.player_list_widget)
		layout.addRow(self.player_btns_widget)
		self.setLayout(layout)

		self.update()

	def update(self):
		self.player_list.clearContents()

		players = [to.players[player] for player in to.sorted_players(self.sort_order)]

		index = 0
		for player in players:
			if index == self.player_list.rowCount():
				self.player_list.insertRow(index)
			name_item = QTableWidgetItem(player.name)
			name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
			self.player_list.setItem(index, 0, name_item)
			record_item = QTableWidgetItem(player.record_str())
			record_item.setFlags(record_item.flags() & ~Qt.ItemIsEditable)
			self.player_list.setItem(index, 1, record_item)
			index += 1
		self.player_list.show()

	def sort_by_name(self):
		self.sort_order = 'by_name'
		self.update()

	def sort_by_rank(self):
		self.sort_order = 'by_rank'
		self.update()

	def player_added(self, player):
		try:
			to.add_player(player)
		except TournamentException as ex:
			self.error = ErrorMessage(str(ex), '')
			self.error.setStyleSheet(style.style_loader.stylesheet)
			self.error.show()
		self.update()

	def player_removed(self, player):
		try:
			to.remove_player(player)
		except TournamentException as ex:
			self.error = ErrorMessage(str(ex), '')
			self.error.setStyleSheet(style.style_loader.stylesheet)
			self.error.show()
		self.update()

	def report_result(self, player, record, win_or_draw):
		pass

	def result_reported(self):
		self.update()

	def pairings_created(self):
		self.update()

	def reset(self):
		self.update()
