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


class LinkedList:

	def __init__(self):
		self.length = 0
		self.head = None

	def print_backward(self):
		print "[",
		if self.head != None:
			self.head.print_backward()
		print "]",

	def add_first(self, cargo):
		node = Node(cargo)
		node.next = self.head
		self.head = node
		self.length += 1


def print_list(node):
	print "[",
	while node:
		if node.next:
			print node,
			print ",",
		else:
			print node,
		node = node.next
	print "]"

def print_backward(list):
	if list == None:
		return
	head = list
	tail = list.next
	print_backward(tail)
	print head,

def remove_second(list):
	if list == None:
		return
	first = list
	second = list.next
	# make the first node refer to the third
	first.next = second.next
	# separate the second node from the rest of the list
	second.next = None
	return second

def print_backward_nicely(list):
	print "[",
	if list != None:
		head = list
		tail = list.next
		print_backward(tail)
		print head,
	print "]",
