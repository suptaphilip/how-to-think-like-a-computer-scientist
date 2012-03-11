class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def coordinates(self):
		return '(%d, %d)' % (self.x, self.y)

	def distance_from_origin(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

def distance(point1, point2):
	return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
