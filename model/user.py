#!/usr/bin/env python3

class User(object):
	def __init__(self, uid=0, name=None, match_wins=0, match_losses=0, match_draws=0):
		self.id = uid
		self.name = name
		self.match_wins = match_wins
		self.match_losses = match_losses
		self.match_draws = match_draws

	def asObject(self):
		return \
			{
				'id': self.id,
				'name': self.name,
				'match_wins':self.match_wins,
				'match_losses': self.match_losses,
				'match_draws': self.match_draws
			}

	def record(self):
		return (self.match_wins, self.match_losses, self.match_draws)

	def record_str(self):
		return '%d-%d-%d' % self.record()

	def __str__(self):
		return 'ID: %d\nName: %s\nRecord: %d/%d/%d' \
			% (self.id, self.name, self.match_wins, self.match_losses, self.match_draws)
