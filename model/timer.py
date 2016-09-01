#!/usr/bin/env python

from time import *

class Timer(object):
	def __init__(self):
		self._start = -1
		self._end = -1
		self._time = 0
		self.formatted = False

	def start(self):
		self._end = -1
		self._start = int(time())
		return self

	def stop(self):
		self._end = int(time())
		return self

	def set(self, time):
		self.reset()
		self._time = time
		return self

	def reset(self):
		self._start = -1
		self._end = -1

	def withFormatting(self, formatted=True):
		self.formatted = formatted
		return self

	def elapsed(self, allowFormatted=True):
		elapsed = -1
		if self._start == -1:
			elapsed = 0
		elif self._end == -1:
			elapsed = (int(time()) - self._start)
		else:
			elapsed = (self._end - self._start)

		if allowFormatted and self.formatted:
			elapsed = self.format(elapsed)

		return elapsed

	def remaining(self, allowFormatted=True):
		remaining = (self._time - self.elapsed(allowFormatted=False))

		if remaining < 0:
			remaining = 0

		if allowFormatted and self.formatted:
			remaining = self.format(remaining)

		return remaining

	def format(self, time):
		SECONDS_PER_HOUR = 3600
		SECONDS_PER_MINUTE = 60

		hours = int(time / SECONDS_PER_HOUR)
		time -= hours * SECONDS_PER_HOUR
		minutes = int(time / SECONDS_PER_MINUTE)
		time -= minutes * SECONDS_PER_MINUTE
		seconds = int(time)

		timeString = []
		if hours > 0:
			timeString.append(str(hours))
			timeString.append(":")

		if minutes < 10:
			timeString.append('0')
		timeString.append(str(minutes))
		timeString.append(":")

		if seconds < 10:
			timeString.append('0')
		timeString.append(str(seconds))

		return ''.join(timeString)

if __name__ == '__main__':
	timer = Timer().withFormatting(True).set(3600)
	print timer.elapsed()
	print timer.remaining()
	timer.start()
	for i in range(5):
		sleep(1)
		print timer.elapsed()
		print timer.remaining()
	timer.stop()
	sleep(1)
	print timer.elapsed()
	print timer.remaining()
