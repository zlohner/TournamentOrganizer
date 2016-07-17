#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

import style.style_loader
from view.pairings_widget import PairingsWidget
from view.report_result_widget import ReportResultWidget

class PairingsWindow(QtGui.QMainWindow):
	def __init__(self):
		super(PairingsWindow, self).__init__()

		# self.setWindowTitle('Pairings')
		self.setStyleSheet(style.style_loader.stylesheet)

		self.pairings_widget = PairingsWidget(self)
		self.setCentralWidget(self.pairings_widget)

		self.report_result_widget = ReportResultWidget()

		self.show()
		self.setFixedWidth(self.width())
		self.setFixedHeight(self.height())

	def show_report_result_widget(self):
		self.report_result_widget.show()
