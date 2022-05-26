#!/usr/bin/env python3

import random
import sqlite3

from model.user import User

class UserManager(object):
	def __init__(self):
		self.connection = sqlite3.connect('db/tournament_organizer.db')
		self.connection.row_factory = sqlite3.Row

	def users(self):
		c = self.connection.cursor()
		users = c.execute('SELECT * FROM users')
		return [User(row['id'], row['name'], row['match_wins'], row['match_losses'], row['match_draws']) for row in users]

	def user(self, uid):
		c = self.connection.cursor()
		row = c.execute('SELECT * FROM users WHERE id = ?', (uid,)).fetchone()
		return User(row['id'], row['name'], row['match_wins'], row['match_losses'], row['match_draws'])

	def decks(self, uid):
		c = self.connection.cursor()
		decks = c.execute('SELECT * FROM decks WHERE user_id = ?', (uid,))
		return [Deck(row['id'], row['user_id'], row['colors'], row['strategy'], row['archetype']) for row in decks]

	def save_user(self, user):
		c = self.connection.cursor()
		db_user = c.execute('SELECT * FROM users WHERE id = ?', (user.id,)).fetchone()
		if db_user:
			c.execute( \
				'UPDATE users SET name = ?, match_wins = ?, match_losses = ?, match_draws = ? WHERE id = ?', \
				(user.name, user.match_wins, user.match_losses, user.match_draws, user.id) \
			)
		else:
			ids = [row[0] for row in c.execute('SELECT id FROM users')]
			new_id = None
			while new_id == None or new_id in ids:
				new_id = random.randint(10000, 99999)
			user.id = new_id
			c.execute(
				'INSERT INTO users(id, name, match_wins, match_losses, match_draws) VALUES (?, ?, ?, ?, ?)', \
				(user.id, user.name, user.match_wins, user.match_losses, user.match_draws) \
			)
		self.connection.commit()


# TODO: Remove this when construction complete

if __name__ == '__main__':
	manager = UserManager()

	name = input()
	bill = User(None, name, 0, 0, 0)
	manager.save_user(bill)

	# users = manager.users()
	# for user in users:
	# 	user.match_wins += 1
	# 	print(str(user))
	# 	manager.save(user)

um = UserManager()
