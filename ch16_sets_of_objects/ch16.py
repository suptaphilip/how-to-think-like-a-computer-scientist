class Card:

	suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	ranks = ['narf', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
				'Jack', 'Queen', 'King']

	def __init__(self, suit=0, rank=0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (self.ranks[self.rank], self.suits[self.suit])

	def __cmp__(self, other):
		# check the suits
		if self.suit > other.suit:
			return 1
		if self.suit < other.suit:
			return -1

		# aces have the highest rank
		if self.rank == 1:
			return 1

		# suits are the same... check ranks
		if self.rank > other.rank:
			return 1
		if self.rank < other.rank:
			return -1

		# ranks are the same... it's a tie
		return 0

class Deck:

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards.append(Card(suit, rank))

	def __str__(self):
		s = ""
		for i in range(len(self.cards)):
			s = s + " " * i + str(self.cards[i]) + "\n"
		return s

	def shuffle(self):
		import random
		num_cards = len(self.cards)
		for i in range(num_cards):
			j = random.randrange(i, num_cards)
			self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

	def remove(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return True
		else:
			return False

	def pop(self):
		return self.cards.pop()

	def is_empty(self):
		return (len(self.cards) == 0)

