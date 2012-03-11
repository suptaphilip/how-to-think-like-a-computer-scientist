#!/usr/bin/env python

# letter_counts.py

import sys

text = sys.argv[1]
counts = {}
for letter in text:
	if letter.isalpha():
		counts[letter.lower()] = counts.get(letter.lower(), 0) + 1
count_items = counts.items()
count_items.sort()
for item in count_items:
    print "%s %d" % (item[0], item[1])
