#!/usr/bin/env python3

observers = []

def update():
	for o in observers:
		o.update()

def player_added(player, user):
	for o in observers:
		o.player_added(player, user)

def player_removed(player):
	for o in observers:
		o.player_removed(player)

def pairings_created():
	for o in observers:
		o.pairings_created()

def report_result(player, record, win_or_draw):
	for o in observers:
		o.report_result(player, record, win_or_draw)

def result_reported():
	for o in observers:
		o.result_reported()

def reset():
	for o in observers:
		o.reset()
