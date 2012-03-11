class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)

	def print_backward(self):
		if self.next != None:
			tail = self.next
			tail.print_backward()
		print self.cargo,


class Queue:
	def __init__(self):
		self.length = 0
		self.head = None

	def is_empty(self):
		return (self.length == 0)

	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.head == None:
			# if list is empty the new node goes first
			self.head = node
		else:
			# find the last node in the list
			last = self.head
			while last.next:
				last = last.next
			# append the new node
			last.next = nod
		self.length += 1

	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length = self.length - 1
		return cargo


class ImprovedQueue:
	def __init__(self):
		self.length = 0
		self.head = None
		self.last = None

	def is_empty(self):
		return (self.length == 0)

	def insert(self, cargo):
		node = Node(cargo)
		node.next = None
		if self.length == 0:
			# if list is empty, the new node is head and last
			self.head = self.last = node
		else:
			# find the last node
			last = self.last
			# append the new node
			last.next = node
			self.last = node
		self.length += 1

	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.last = None
		return cargo


class PriorityQueue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def insert(self, item):
		self.items.append(item)

	def remove(self):
		maxi = 0
		for i in range(1, len(self.items)):
			if self.items[i] > self.items[maxi]:
				maxi = i
		item = self.items[maxi]
		self.items[maxi:maxi + 1] = []
		return item


class Golfer:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def __str__(self):
		return "%-16s: %d" % (self.name, self.score)

	def __cmp__(self, other):
		if self.score < other.score:
			return 1		# less is more
		if self.score > other.score:
			return -1
		return 0
