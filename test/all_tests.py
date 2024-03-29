#!/usr/bin/env python3

import unittest

from test.tournament_organizer_test import TournamentOrganizerTest
from model.tournament_exception import TournamentException

def runTests():
	tournament_organizer_tests = unittest.TestLoader().loadTestsFromTestCase(TournamentOrganizerTest)
	all_tests = unittest.TestSuite([tournament_organizer_tests])

	result = unittest.TestResult()
	all_tests.run(result)

	if not result.wasSuccessful():
		for test, trace in result.failures + result.errors:
			print(str(test) + '\n' + trace)
		raise TournamentException('tests not succesful')
