#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
import view.notifier
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

class PairingsWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(PairingsWidget, self).__init__(parent)
		self.parent = parent

		view.notifier.observers.append(self)

		self.header_label = QtGui.QLabel('Pairings')

		self.header_widget = QtGui.QWidget(self)
		header_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
		header_layout.addWidget(self.header_label)
		self.header_widget.setLayout(header_layout)

		self.pairings_list = QtGui.QTableWidget(style.style_loader.TABLE_INITIAL_LENGTH, 2, self)
		self.pairings_list.setFixedHeight(300)
		self.pairings_list.setFixedWidth(400)
		self.pairings_list.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.pairings_list.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)

		self.pairings_list_widget = QtGui.QWidget(self)
		pairings_list_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		pairings_list_layout.addWidget(self.pairings_list)
		self.pairings_list_widget.setLayout(pairings_list_layout)

		self.report_btn = QtGui.QPushButton('Report Results', self)
		self.report_btn.clicked.connect(parent.show_report_result_widget)

		self.report_btn_widget = QtGui.QWidget(self)
		report_btn_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		report_btn_layout.addWidget(self.report_btn)
		self.report_btn_widget.setLayout(report_btn_layout)

		layout = QtGui.QFormLayout()
		layout.addRow(self.header_widget)
		layout.addRow(self.pairings_list_widget)
		layout.addRow(self.report_btn_widget)
		self.setLayout(layout)

		self.update()

	def update(self):
		self.pairings_list.clearContents()

		index = 0
		for p1, p2 in to.pairings.iteritems():
			if index == self.pairings_list.rowCount():
				self.pairings_list.insertRow(index)
			p1_item = QtGui.QTableWidgetItem(p1)
			p1_item.setFlags(p1_item.flags() & ~QtCore.Qt.ItemIsEditable)
			self.pairings_list.setItem(index, 0, p1_item)
			if p2 == None:
				p2_str = '--BYE--'
			else:
				p2_str = p2
			p2_item = QtGui.QTableWidgetItem(p2_str)
			p2_item.setFlags(p2_item.flags() & ~QtCore.Qt.ItemIsEditable)
			self.pairings_list.setItem(index, 1, p2_item)
			index += 1
		self.pairings_list.show()

	def player_added(self, player):
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
