#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
import view.notifier
from model.tournament_organizer import to
from model.tournament_exception import TournamentException
from view.error_message import ErrorMessage

class RoundManagerWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(RoundManagerWidget, self).__init__(parent)
		self.parent = parent

		self.sort_order = 'by_name'

		view.notifier.observers.append(self)
		timer = QtCore.QTimer(self)
		timer.timeout.connect(self.update)
		timer.start()

		self.header_label = QtGui.QLabel('Round')

		self.header_widget = QtGui.QWidget(self)
		header_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		header_layout.addWidget(self.header_label)
		self.header_widget.setLayout(header_layout)

		self.submit_btn = QtGui.QPushButton(self)
		self.submit_btn.clicked.connect(self.submit)

		self.submit_btn_widget = QtGui.QWidget(self)
		submit_btn_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		submit_btn_layout.addWidget(self.submit_btn)
		self.submit_btn_widget.setLayout(submit_btn_layout)

		self.round_info = QtGui.QLabel()
		self.round_info.setAlignment(QtCore.Qt.AlignHCenter)
		self.timer_display = QtGui.QLabel()
		self.timer_display.setAlignment(QtCore.Qt.AlignHCenter)

		self.info_widget = QtGui.QWidget(self)
		info_layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
		info_layout.addWidget(self.round_info)
		info_layout.addWidget(self.timer_display)
		self.info_widget.setLayout(info_layout)

		self.error = None

		layout = QtGui.QFormLayout()
		layout.addRow(self.header_widget)
		layout.addRow(self.submit_btn_widget)
		layout.addRow(self.info_widget)
		self.setLayout(layout)

		self.update()

	def update(self):
		self.round_info.setText('Round ' + str(to.round_num) + '/' + str(to.rounds))
		self.timer_display.setText('Time ' + str(to.timer.remaining()))
		if len(to.pairings) > 0:
			self.submit_btn.setText('Round In Progress')
			self.submit_btn.setEnabled(False)
		elif to.round_num == 0:
			self.submit_btn.setText('Start Tournament')
			self.submit_btn.setEnabled(True)
		elif to.round_num == to.rounds:
			to.timer.reset()
			self.submit_btn.setText('Tournament Ended - Reset')
			self.submit_btn.setEnabled(True)
		else:
			to.timer.reset()
			self.submit_btn.setText('Start Round')
			self.submit_btn.setEnabled(True)

	def submit(self):
		if to.rounds > 0 and to.round_num == to.rounds:
			to.reset()
			view.notifier.reset()
		else:
			try:
				to.make_pairings()
				to.lock_pairings()
				view.notifier.pairings_created()
			except TournamentException as ex:
				self.error = ErrorMessage(str(ex), '')
				self.error.setStyleSheet(style.style_loader.stylesheet)
				self.error.show()

	def player_added(self, player):
		pass

	def player_removed(self, player):
		pass

	def report_result(self, player, record, win_or_draw):
		pass

	def result_reported(self):
		self.update()

	def pairings_created(self):
		self.update()

	def reset(self):
		self.update()
