#!/usr/bin/env python

import unittest
import random
import math

from model.tournament_organizer import to
from model.tournament_exception import TournamentException

def pairings():
	pairings = []
	printed = []
	for p1, p2 in to.pairings.iteritems():
		if p1 not in printed:
			if p2 == None:
				pairings.append(str(to.players[p1]) + ' - BYE\n')
				printed.append(p1)
			else:
				pairings.append(str(to.players[p1]) + ' - ' + str(to.players[p2]) + '\n')
				printed.append(p1)
				printed.append(p2)
	return ''.join(pairings)

def players():
	players = []
	for name in to.sorted_players('by_rank'):
		players.append(str(to.players[name]) + '\n')
	return ''.join(players)

def play_random_match(to, player, opponent):
	will_draw = random.random()
	r = random.random()
	if will_draw < 0.05:
		if r < 0.8:
			record = (1, 1, 1)
		elif r < 0.98:
			record = (0, 0, 1)
		else:
			record = (0, 0, 2)
		to.record_draw(player, record)
	else:
		if r < 0.45:
			record = (2, 0, 0)
		elif r < 0.9:
			record = (2, 1, 0)
		elif r < 0.96:
			record = (1, 0, 0)
		elif r < 0.98:
			record = (2, 0, 1)
		else:
			record = (2, 1, 1)
		to.record_win(player, record)

def run_random_tournament(NUM_PLAYERS, DROP_AFTER_ROUND=0, PRINT_OUTPUT=False):
	ROUNDS = int(math.ceil(math.log(NUM_PLAYERS, 2)))

	if PRINT_OUTPUT:
		print ''
		print NUM_PLAYERS,'Players'
		print ROUNDS,'Rounds'
		print ''

	to.reset()

	for PLAYER_NAME in range(1, NUM_PLAYERS + 1):
		to.add_player(str(PLAYER_NAME))

	for ROUND in range(1, ROUNDS + 1):
		if PRINT_OUTPUT:
			print players()

		to.make_pairings()

		if PRINT_OUTPUT:
			print 'R' + str(ROUND) + ':'
			print pairings()

		bye_count = 0
		for player, opponent in to.pairings.iteritems():
			if opponent == None:
				bye_count += 1
		expected_byes = len(to.players) % 2
		if not len(to.players) % 2 == bye_count:
			raise TournamentException('Wrong number of byes: expected ' + str(expected_byes) + ', was ' + str(bye_count))

		played_count = 0
		for player, opponent in to.pairings.iteritems():
			if opponent in to.players[player].opponents:
				played_count += 1
				if PRINT_OUTPUT:
					print player + ' has already played ' + opponent

		if not played_count == 0:
			raise TournamentException('Pairing made for pair that have already played')

		for name, player in to.players.iteritems():
			if len(player.opponents) < to.round_num - 1:
				print 'WARNING: Player received multiple byes'
				# print 'Player:',str(player),'Opponents:',[str(opponent) for opponent in player.opponents]
				# print 'Standings:'
				# print players()

		to.lock_pairings()

		played = []
		round_pairings = [(player, opponent) for player, opponent in to.pairings.iteritems()]
		for player, opponent in round_pairings:
			if opponent == None:
				to.record_win(player, (2,0,0))
			elif player not in played:
				play_random_match(to, player, opponent)
				played.append(player)
				played.append(opponent)

		for NUM_TO_DROP in range(DROP_AFTER_ROUND):
			if len(to.players) > 0:
				to.remove_player(to.sorted_players()[-1])

	if PRINT_OUTPUT:
		print 'Results:'
		print players()

def run_multiple_tournaments(NUM_TOURNAMENTS, RANGE_START, RANGE_END):
	for i in range(NUM_TOURNAMENTS / 2):
		r = random.randint(RANGE_START, RANGE_END)
		run_random_tournament(
			r,
			PRINT_OUTPUT=False
		)
		run_random_tournament(
			r,
			DROP_AFTER_ROUND=random.randint(0, max(1, int(r * 0.1))),
			PRINT_OUTPUT=False
		)
	if NUM_TOURNAMENTS % 2 == 1:
		run_random_tournament(
			random.randint(RANGE_START, RANGE_END),
			PRINT_OUTPUT=True
		)

class TournamentOrganizerTest(unittest.TestCase):
	def test_small_tournaments(self):
		NUM_SMALL_TOURNAMENTS = 98
		SMALL_RANGE_START = 7
		SMALL_RANGE_END = 32
		print 'Small: %d tournaments, %d - %d players' % (NUM_SMALL_TOURNAMENTS, SMALL_RANGE_START, SMALL_RANGE_END),'...'
		run_multiple_tournaments(NUM_SMALL_TOURNAMENTS, SMALL_RANGE_START, SMALL_RANGE_END)
		print 'Success!'

	def test_medium_tournaments(self):
		NUM_MEDIUM_TOURNAMENTS = 32
		MEDIUM_RANGE_START = 64
		MEDIUM_RANGE_END = 100
		print 'Medium: %d tournaments, %d - %d players' % (NUM_MEDIUM_TOURNAMENTS, MEDIUM_RANGE_START, MEDIUM_RANGE_END),'...'
		run_multiple_tournaments(NUM_MEDIUM_TOURNAMENTS, MEDIUM_RANGE_START, MEDIUM_RANGE_END)
		print 'Success!'

	def test_large_tournaments(self):
		NUM_LARGE_TOURNAMENTS = 2
		LARGE_RANGE_START = 120
		LARGE_RANGE_END = 300
		print 'Large: %d tournaments, %d - %d players' % (NUM_LARGE_TOURNAMENTS, LARGE_RANGE_START, LARGE_RANGE_END),'...'
		run_multiple_tournaments(NUM_LARGE_TOURNAMENTS, LARGE_RANGE_START, LARGE_RANGE_END)
		print 'Success!'

if __name__ == '__main__':
		unittest.main()
