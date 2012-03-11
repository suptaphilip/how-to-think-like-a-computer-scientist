class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def insert(self, item):
		self.items.append(item)

	def remove(self):
		return self.items.pop(0)


class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)


class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def add_first(self, cargo):
		node = Node(cargo)
		node.next = self.head
		self.head = node
		self.length += 1


class PriorityQueue:
	def __init__(self):
		self.length = 0

	def is_empty(self):
		return self.length == 0

	def insert(self, item):
		node = Node(item)
		if self.is_empty()
