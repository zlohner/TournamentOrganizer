#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
from view.tournament_organizer_widget import TournamentOrganizerWidget
from view.add_player_widget import AddPlayerWidget
from view.remove_player_widget import RemovePlayerWidget
from view.pairings_window import PairingsWindow
from view.round_manager_window import RoundManagerWindow

class TournamentOrganizerWindow(QtGui.QMainWindow):
	def __init__(self):
		super(TournamentOrganizerWindow, self).__init__()

		# self.setWindowTitle('Tournament Organizer')
		self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(style.style_loader.ICON_FILENAME_JPG)))
		self.setStyleSheet(style.style_loader.stylesheet)

		self.tournament_organizer_widget = TournamentOrganizerWidget(self)
		self.setCentralWidget(self.tournament_organizer_widget)
		self.move(150, 100)

		self.add_player_widget = AddPlayerWidget()
		self.remove_player_widget = RemovePlayerWidget()
		self.pairings_window = PairingsWindow()
		self.round_manager_window = RoundManagerWindow()

		self.create_menu_bar()

		self.show()
		self.setFixedWidth(self.width())
		self.setFixedHeight(self.height())

	def create_menu_bar(self):
		self.menu_bar = QtGui.QMenuBar(self)

		self.player_menu = QtGui.QMenu('Players', self)
		self.player_menu.addAction('Add Player', self.show_add_player_widget)
		self.player_menu.addAction('Remove Player', self.show_remove_player_widget)
		# self.player_menu.addAction('Random Seating', self.randomize_players) TODO: make random pairing window

		self.pairings_menu = QtGui.QMenu('Pairings', self)
		self.pairings_menu.addAction('Make Pairings')

		self.menu_bar.addMenu(self.player_menu)
		self.menu_bar.addMenu(self.pairings_menu)

	def show_add_player_widget(self):
		self.add_player_widget.show()

	def show_remove_player_widget(self):
		self.remove_player_widget.show()
