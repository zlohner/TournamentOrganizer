#!/usr/bin/env python

WIN_MATCH_POINTS = 3
LOSE_MATCH_POINTS = 0
DRAW_MATCH_POINTS = 1

import sys
import random
import numpy
from sets import Set

class Player(object):
	def __init__(self, name):
		self.name = name
		self.match_wins = 0
		self.match_losses = 0
		self.match_draws = 0
		self.game_wins = 0
		self.game_losses = 0
		self.game_draws = 0
		self.opponents = Set()
		self.sort_constant = random.randint(1, sys.maxint)

	def add_record(self, record):
		game_wins, game_losses, game_draws = record
		self.game_wins += game_wins
		self.game_losses += game_losses
		self.game_draws += game_draws

	def record_win(self, record):
		self.add_record(record)
		self.match_wins += 1

	def record_loss(self, record):
		self.add_record(record)
		self.match_losses += 1

	def record_draw(self, record):
		self.add_record(record)
		self.match_draws += 1

	def match_points(self):
		return \
			WIN_MATCH_POINTS * self.match_wins + \
			DRAW_MATCH_POINTS * self.match_draws + \
			LOSE_MATCH_POINTS * self.match_losses

	def match_win_percent(self):
		matches = self.match_wins + self.match_losses + self.match_draws
		if matches == 0:
			return 0
		else:
			return float(self.match_wins) / float(matches)

	def game_win_percent(self):
		games = self.game_wins + self.game_losses + self.game_draws
		if games == 0:
			return 0
		else:
			return float(self.game_wins) / float(games)

	def played(self, player):
		return player in self.opponents

	def __eq__(self, other):
		return other != None and self.name == other.name

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		val = 0
		for c in self.name:
			val += ord(c)
			val *= 31
		return val

	def __lt__(self, other):
		self_OMWP = 1
		other_OMWP = 1

		if len(self.opponents) > 0:
			self_OMWP = numpy.mean([opp.match_win_percent() for opp in self.opponents])
		if len(other.opponents) > 0:
			other_OMWP = numpy.mean([opp.match_win_percent() for opp in other.opponents])

		self_GWP = self.game_win_percent()
		other_GWP = other.game_win_percent()

		if self.match_points() > other.match_points():
			return True
		elif self.match_points() == other.match_points() \
		and self_OMWP > other_OMWP:
			return True
		elif self.match_points() == other.match_points() \
		and self_OMWP == other_OMWP \
		and self_GWP > other_GWP:
			return True
		elif self.match_points() == other.match_points() \
		and self_OMWP == other_OMWP \
		and self_GWP == other_GWP \
		and self.sort_constant < other.sort_constant:
			return True
		else:
			return False

	def record_str(self):
		return str(self.match_wins) + '-' + str(self.match_losses) + '-' + str(self.match_draws)

	def formatted(self):
		return self.name + '\t\t  ' + self.record_str()

	def __str__(self):
		return '(' + self.name + ' - ' + self.record_str() + ')'
