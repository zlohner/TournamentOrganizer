#!/usr/bin/env python3

import sys
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication
import argparse

import style.style_loader
from test.all_tests import runTests
from view.tournament_organizer_window import TournamentOrganizerWindow

def parseArgs():
	parser = argparse.ArgumentParser(\
		prog='TournamentOrganizer', \
		description='An app for organizing and running swiss style tournaments', \
		add_help=True)
	parser.add_argument('-t', '--test', action='store_true', help='run tests', default=False)
	return parser.parse_args()

def run():
	app = QApplication(sys.argv)
	QFontDatabase.addApplicationFont('./style/' + style.style_loader.FONT + '.ttf')
	to_window = TournamentOrganizerWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	args = parseArgs()
	if args.test:
		runTests()
	else:
		run()
