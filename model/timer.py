from time import *

class Timer(object):
	def __init__(self):
		self._start = 0
		self._end = -1
		self._time = 0
		self.formatted = False

	def start(self):
		self._start = time()

	def stop(self):
		self._end = time()

	def set(self, time):
		self._time = time

	def withFormatting(self, formatted):
		self.formatted = formatted

	def elapsed(self, allowFormatted=True):
		elapsed = -1
		if self._end == -1:
			elapsed = (time() - self._start)
		else:
			elapsed = (self._end - self._start)

		if allowFormatted and self.formatted:
			elapsed = self.format(elapsed)

		return elapsed

	def remaining(self, allowFormatted=True):
		remaining = (self._time - self.elapsed(allowFormatted=False))
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
	timer = Timer()
	timer.set(7200)
	timer.withFormatting(True)
	timer.start()
	sleep(1)
	print timer.elapsed()
	print timer.remaining()
	sleep(1)
	print timer.elapsed()
	print timer.remaining()
	timer.stop()
	sleep(1)
	print timer.elapsed()
	print timer.remaining()
