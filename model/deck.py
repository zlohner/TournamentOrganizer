#!/usr/bin/env python3

class Deck(object):
	def __init__(self, did=0, uid=0, colors='', strategy='', archetype=''):
		self.id = did
		self.uid = uid
		self.colors = colors
		self.strategy = strategy
		self.archetype = archetype

	def asObject(self):
		return \
			{
				'id': self.id,
				'uid': self.uid,
				'colors': self.colors,
				'strategy': self.strategy,
				'archetype': self.archetype,
			}

	def __str__(self):
		return 'ID: %d\nUser ID: %d\nColors: %s\nStrategy: %s\nArchetype: %s' \
			% (self.id, self.uid, self.colors, self.strategy, self.archetype)
