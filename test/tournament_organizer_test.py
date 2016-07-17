#!/usr/bin/env python

import unittest
import random
import math

from model.tournament_organizer import TournamentOrganizer

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

class TournamentOrganizerTest(unittest.TestCase):
	def test_tournament(self):
		print ''

		NUM_PLAYERS = random.randint(7, 32)
		ROUNDS = int(math.ceil(math.log(NUM_PLAYERS, 2)))

		print NUM_PLAYERS,'Players'
		print ROUNDS,'Rounds'

		to = TournamentOrganizer()
		to.rounds = ROUNDS

		for PLAYER_NAME in range(1, NUM_PLAYERS + 1):
			to.add_player(str(PLAYER_NAME))
		print ''

		for ROUND in range(1, to.rounds + 1):
			print '[',
			for name in to.sorted_players():
				print to.players[name],
			print ']'
			print ''

			to.make_pairings()

			bye_count = 0
			for player, opponent in to.pairings.iteritems():
				if opponent == None:
					bye_count += 1
			self.assertTrue(bye_count <= 1)

			played_count = 0
			for player, opponent in to.pairings.iteritems():
				if opponent in to.players[player].opponents:
					played_count += 1
			self.assertTrue(played_count == 0)

			printed = []
			print 'R' + str(ROUND) + ':'
			for p1, p2 in to.pairings.iteritems():
				if p1 not in printed:
					if p2 == None:
						print str(to.players[p1]),' - BYE'
						printed.append(p1)
					else:
						print str(to.players[p1]),' - ',str(to.players[p2])
						printed.append(p1)
						printed.append(p2)
			print ''

			played = []
			round_pairings = [(player, opponent) for player, opponent in to.pairings.iteritems()]
			for player, opponent in round_pairings:
				if opponent == None:
					to.record_win(player, (0,0,0))
				elif player not in played:
					play_random_match(to, player, opponent)
					played.append(player)
					played.append(opponent)

			for NUM_TO_DROP in range(random.randint(0,ROUND)):
				to.remove_player(to.sorted_players()[-1])

		print '[',
		for name in to.sorted_players():
			print to.players[name],
		print ']'
		print ''

	def test_multiple_tournaments(self):
		for i in range(10):
			self.test_tournament()

if __name__ == '__main__':
		unittest.main()
