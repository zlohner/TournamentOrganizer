#!/usr/bin/env python3

from PyQt5 import QtGui, QtCore

STYLE_DIRECTORY = './style/'
ICON_FILENAME = STYLE_DIRECTORY + 'tournament_organizer.icns'
ICON_FILENAME_JPG = STYLE_DIRECTORY + 'tournament_organizer.jpg'
SS_FILENAME = STYLE_DIRECTORY + 'styles.css'
FONT = 'Montserrat'
TABLE_INITIAL_LENGTH = 10

replacements = {
	'@bgcolor':'#494248',
	'@fgcolor1':'#a4aaba',
	'@fgcolor2':'#d7dce2',
	'@font':'\'' + FONT + '\'',
}

with open(SS_FILENAME, 'r') as ss_file:
	stylesheet = ss_file.read()
for old, new in replacements.items():
	stylesheet = stylesheet.replace(old, new)
