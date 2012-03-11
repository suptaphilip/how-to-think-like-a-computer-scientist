class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d, %d)' % (self.x, self.y)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return self.x * other.x + self.y * other.y

	def __rmul__(self, other):
		return Point(self.x * other, self.y * other)

	def reverse(self):
		self.x, self.y = self.y, self.x

class Time:

	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def print_time(self):
		print '%d:%d:%d' % (self.hours, self.minutes, self.seconds)

	def increment(self, seconds):
		self.seconds = seconds + self.seconds

		while self.seconds >= 60:
			self.seconds -= 60
			self.minutes += 1

		while self.minutes >= 60:
			self.minutes -= 60
			self.hours += 1

	def after(self, time):
		if self.hours > time.hours:
			return True
		elif self.hours < time.hours:
			return False

		if self.minutes > time.minutes:
			return True
		elif self.minutes < time.minutes:
			return False

		if self.seconds > time.seconds:
			return True
		elif self.seconds < time.seconds:
			return False

	def convert_to_seconds(self):
		minutes = self.hours * 60 + self.minutes
		seconds = minutes * 60 + self.seconds
		return seconds

def find(str, ch, start=0, end=0):
	index = start
	if end == 0:
		end = len(str)
	while index < end:
		if str[index] == ch:
			return index
		index += 1
	return -1

def multadd(x, y, z):
	return x * y + z

def front_and_back(front):
	import copy
	back = copy.copy(front)
	back.reverse()
	print str(front) + str(back)
