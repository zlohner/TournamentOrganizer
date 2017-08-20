#!/usr/bin/env python3

from PyQt5.QtWidgets import QMainWindow

import style.style_loader
from view.pairings_widget import PairingsWidget
from view.report_result_widget import ReportResultWidget

class PairingsWindow(QMainWindow):
	def __init__(self):
		super(PairingsWindow, self).__init__()

		# self.setWindowTitle('Pairings')
		self.setStyleSheet(style.style_loader.stylesheet)
		self.move(1100, 200)

		self.pairings_widget = PairingsWidget(self)
		self.setCentralWidget(self.pairings_widget)

		self.report_result_widget = ReportResultWidget()

		self.show()
		self.setFixedWidth(self.width())
		self.setFixedHeight(self.height())

	def show_report_result_widget(self):
		self.report_result_widget.update()
		self.report_result_widget.show()
