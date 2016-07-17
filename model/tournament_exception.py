#!/usr/bin/env python

class TournamentException(Exception):
	def __init__(self, value):
		super(TournamentException, self).__init__()
		self.value = value
	def __str__(self):
		return str(self.value)
