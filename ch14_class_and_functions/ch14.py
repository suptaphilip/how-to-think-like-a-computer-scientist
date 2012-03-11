class Time:
	pass

def add_time(t1, t2):
	seconds = convert_to_seconds(t1) + convert_to_seconds(t2)
	return make_time(seconds)

def print_time(time):
	print '%d:%d:%d' % (time.hours, time.minutes, time.seconds)

def convert_to_seconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

def make_time(seconds):
	time = Time()
	time.hours = seconds / 3600
	seconds -= time.hours * 3600
	time.minutes = seconds / 60
	seconds -= time.minutes * 60
	time.seconds = seconds
	return time

def after(t1, t2):
	if t1.hours > t2.hours:
		return True
	elif t1.hours < t2.hours:
		return False

	if t1.minutes > t2.minutes:
		return True
	elif t1.minutes < t2.minutes:
		return False

	if t1.seconds > t2.seconds:
		return True
	elif t1.seconds < t2.seconds:
		return False

def increment(time, seconds):
	time_seconds = convert_to_seconds(time) + seconds
	return make_time(time_seconds)
