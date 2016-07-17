#!/usr/bin/env python

observers = []

def player_added(player):
	for o in observers:
		o.player_added(player)

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