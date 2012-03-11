class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.cargo)

def total(tree):
	if tree == None:
		return 0
	return total(tree.left) + total(tree.right) + tree.cargo

def print_tree_preorder(tree):
	if tree == None:
		return
	print tree.cargo,
	print_tree_preorder(tree.left)
	print_tree_preorder(tree.right)

def print_tree_postorder(tree):
	if tree == None:
		return
	print_tree_postorder(tree.left)
	print_tree_postorder(tree.right)
	print tree.cargo,

def print_tree_inorder(tree):
	if tree == None:
		return
	print_tree_inorder(tree.left)
	print tree.cargo,
	print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
	if tree == None:
		return
	print_tree_indented(tree.right, level + 1)
	print '  ' * level + str(tree.cargo)
	print_tree_indented(tree.left, level + 1)

def get_token_list(expr):
	return expr.split()

def get_token(token_list, expected):
	if token_list[0] == expected:
		del token_list[0]
		return True
	else:
		return False

def get_number(token_list):
	x = token_list[0]
	if type(x) != type(0):
		return None
	del token_list[0]
	return Tree(x, None, None)

def get_number(token_list):
	if get_token(token_list, '('):
		x = get_sum(token_list)
		if not get_token(token_list, ')'):
			raise 'BadExpressionError', 'missing parenthesis'
		return x
	else:
		x = token_list[0]
		if type(x) != type(0):
			return None
		token_list[:1] = []
		return Tree(x, None, None)

def get_product(token_list):
	a = get_number(token_list)
	if get_token(token_list, '*'):
		b = get_product(token_list)
		return Tree('*', a, b)
	else:
		return a

def get_sum(token_list):
	a = get_product(token_list)
	if get_token(token_list, '+'):
		b = get_sum(token_list)
		return Tree('+', a, b)
	else:
		return a

def yes(ques):
	ans = raw_input(ques).lower()
	return ans[0] == 'y'

def animal():
	# start with a singleton
	root = Tree("bird")

	# loop until the user quits
	while True:
		print
		if not yes("Are you thinking of an animal? "):
			break

		# walk the tree
		tree = root
		while tree.left != None:
			prompt = tree.cargo + "? "
			if yes(prompt):
				tree = tree.right
			else:
				tree = tree.left

		# make a guess
		guess = tree.cargo
		prompt = "Is it a " + guess + "? "
		if yes(prompt):
			print "I rule!"
			continue

		# get new information
		prompt = "What is the animal's name? "
		animal = raw_input(prompt)
		prompt = "What question whould distinguish a %s from a %s? "
		question = raw_input(prompt % (animal, guess))

		# add new information to the tree
		tree.cargo = question
		prompt = "If the animal were %s the answer would be? "
		if yes(prompt % animal):
			tree.left = Tree(guess)
			tree.right = Tree(animal)
		else:
			tree.left = Tree(animal)
			tree.right = Tree(guess)
