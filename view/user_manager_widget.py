#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QLabel, QBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QFormLayout

import style.style_loader
import view.notifier
from model.user_manager import um
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

class UserManagerWidget(QWidget):
	def __init__(self, parent):
		super(UserManagerWidget, self).__init__(parent)
		self.parent = parent

		self.sort_order = 'by_name'

		view.notifier.observers.append(self)

		self.header_label = QLabel('Users')

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

		self.user_list = QTableWidget(style.style_loader.TABLE_INITIAL_LENGTH, 3, self)
		self.user_list.setFixedHeight(300)
		self.user_list.setFixedWidth(400)
		self.user_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.user_list.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

		self.user_list_widget = QWidget(self)
		user_list_layout = QBoxLayout(QBoxLayout.LeftToRight)
		user_list_layout.addWidget(self.user_list)
		self.user_list_widget.setLayout(user_list_layout)

		self.add_player_btn = QPushButton('Add User', self)
		self.add_player_btn.clicked.connect(self.parent.show_add_user_widget)
		self.remove_player_btn = QPushButton('Remove User', self)
		self.remove_player_btn.clicked.connect(self.parent.show_remove_user_widget)

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
		layout.addRow(self.user_list_widget)
		layout.addRow(self.player_btns_widget)
		self.setLayout(layout)

		self.update()

	def update(self):
		self.user_list.clearContents()
		# TODO: get the most recent user list
		users = um.users()

		index = 0
		for user in users:
			if index == self.user_list.rowCount():
				self.user_list.insertRow(index)
			name_item = QTableWidgetItem(user.name)
			name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
			self.user_list.setItem(index, 0, name_item)
			id_item = QTableWidgetItem(str(user.id))
			id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
			self.user_list.setItem(index, 1, id_item)
			record_item = QTableWidgetItem(user.record_str())
			record_item.setFlags(record_item.flags() & ~Qt.ItemIsEditable)
			self.user_list.setItem(index, 2, record_item)
			index += 1
		self.user_list.show()

	def sort_by_name(self):
		self.sort_order = 'by_name'
		self.update()

	def sort_by_rank(self):
		self.sort_order = 'by_rank'
		self.update()

	def player_added(self, player, user):
		self.update()

	def player_removed(self, player):
		self.update()

	def report_result(self, player, record, win_or_draw):
		pass

	def result_reported(self):
		self.update()

	def pairings_created(self):
		self.update()

	def reset(self):
		self.update()
