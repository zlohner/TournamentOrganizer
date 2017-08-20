#!/usr/bin/env python3

import random
import math
import time

from model.player import Player
from model.timer import Timer
from model.tournament_exception import TournamentException
from model.user_manager import um

class TournamentOrganizer(object):
	def __init__(self):
		self.players = {}
		self.pairings = {}
		self.round_num = 0
		self.rounds = 0
		self.timer = Timer()

	def add_player(self, name, user):
		if user.id in [player.user.id for player in self.players.values()]:
			raise TournamentException(user.name + '#' + str(user.id) + ' has already been added')
		elif user.name in self.players:
			existing_player = self.players[user.name]
			self.players.pop(user.name)

			new_tag = existing_player.name + '#' + str(existing_player.user.id)
			existing_player.name = new_tag
			self.players[new_tag] = existing_player

			tag = name + '#' + str(user.id)
			self.players[tag] = Player(tag, user)
		else:
			self.players[user.name] = Player(user.name, user)

	def remove_player(self, name):
		if name in self.players:
			um.save_user(self.players[name].user)
			del self.players[name]
		else:
			raise TournamentException(name + ' has not been added yet')

	def record_win(self, winner, record):
		if winner in self.pairings:
			if winner in self.players:
				self.players[winner].record_win(record)
			opponent = self.pairings[winner]
			if not opponent == None and opponent in self.pairings:
				if opponent in self.players:
					self.players[opponent].record_loss(record)
				del self.pairings[opponent]
			del self.pairings[winner]
		else:
			raise TournamentException('Win not recorded, pairing for player ' + winner + ' does not exist')

	def record_loss(self, loser, record):
		if loser in self.pairings.keys():
			if loser in self.players:
				self.players[loser].record_loss(record)
			opponent = self.pairings[loser]
			if not opponent == None and opponent in self.pairings:
				if opponent in self.players:
					self.players[opponent].record_win(record)
				del self.pairings[opponent]
			del self.pairings[loser]
		else:
			raise TournamentException('Win not recorded, pairing for player ' + winner + ' does not exist')

	def record_draw(self, player, record):
		if player in self.pairings:
			if not self.pairings[player] == None and self.pairings[player] in self.pairings:
				player_wins, opp_wins, draws = record
				if player in self.players:
					self.players[player].record_draw(record)
				opponent = self.pairings[player]
				if opponent in self.players:
					self.players[opponent].record_draw((opp_wins, player_wins, draws))
				del self.pairings[player]
				del self.pairings[opponent]
			else:
				raise TournamentException('Draw not recorded, player ' + player + ' has a bye and cannot draw')
		else:
			raise TournamentException('Draw not recorded, pairing for player ' + player + ' does not exist')

	def sorted_players(self, method='by_rank'):
		if method == 'by_rank':
			players = self.players.values()
			return [player.name for player in sorted(players)]
		elif method == 'by_name':
			return [player for player in sorted(self.players.keys())]
		elif method == 'random':
			players = self.players.keys()
			random.shuffle(players)
			return players

	def make_pair(self, p1, p2):
		self.pairings[p1] = p2
		if p2 != None:
			self.pairings[p2] = p1

	def make_restrictions(self):
		restrictions = []
		for p1 in self.players.keys():
			for p2 in self.players[p1].opponents:
				restrictions.append((p1, p2.name))
		return restrictions

	def make_pairings(self):
		if to.round_num == 0 and len(to.players) < 4:
			raise TournamentException('Can\'t start tournament, not enough players')
		if len(self.pairings) > 0:
			raise TournamentException('Can\'t make pairings, round still in progress')

		restrictions = self.make_restrictions()
		restrictions.append(None)
		unpaired_count = 2

		MAX_BYES = len(to.players) % 2
		while unpaired_count > MAX_BYES:

			self.pairings = {}

			restrictions = restrictions[:-1]

			unpaired = self.sorted_players() + [ None ]
			unpaired_count = len(unpaired) - 1

			while len(unpaired) > 1 and not unpaired[0] == None:
				p1 = unpaired[0]
				unpaired = unpaired[1:]

				restricted = []

				paired = False

				while not paired and len(unpaired) > 0:
					p2 = unpaired[0]
					unpaired = unpaired[1:]
					if (p1, p2) in restrictions:
						restricted.append(p2)
					else:
						self.make_pair(p1, p2)
						paired = True
						if p2 == None:
							unpaired_count -= 1
						else:
							unpaired_count -= 2

				unpaired = restricted + unpaired

	def lock_pairings(self):
		if self.round_num == 0:
			self.rounds = int(math.ceil(math.log(len(self.players), 2)))

		self.round_num += 1
		self.timer.set(3000)
		self.timer.start()

		for p1, p2 in self.pairings.items():
			if not p2 == None:
				self.players[p1].opponents.add(self.players[p2])
				self.players[p2].opponents.add(self.players[p1])

	def game_end(self):
		for name, player in self.players.items():
			um.save_user(player.user)

	def reset(self):
		self.players = {}
		self.pairings = {}
		self.round_num = 0
		self.rounds = 0
		self.timer.reset()

to = TournamentOrganizer()
to.timer.withFormatting()
