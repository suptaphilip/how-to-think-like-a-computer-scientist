#!/usr/bin/env python

#
# alice_words.py
#

import string


def get_text(text_file):
	return open(text_file, 'r').read().split()

def get_check_tuple():
	return tuple([letter for letter in string.ascii_lowercase])

def filter_words(input_text, check_tuple):
	output_text = input_text[:]
	for index in reversed(range(len(output_text))):
		if not output_text[index].startswith(check_tuple):	# does not filter the whitespace key
			output_text.remove(output_text[index])
	return output_text

def split_hyphenated_words(input_text):
	output_text = input_text[:]
	for index in reversed(range(len(output_text))):
		if '--' in output_text[index]:
			output_text.extend(output_text[index].split('--'))
			output_text.remove(output_text[index])
	return output_text

def get_word_counts(word_counts, input_text):	# the value for 'a' is 611 instead of 631
	for index in range(len(input_text)):
		word = input_text[index].strip(string.punctuation).lower()
		word_counts[word] = word_counts.get(word, 0) + 1
	return word_counts

def get_counts_list(word_counts):
	counts_list = word_counts.items()
	counts_list.sort()
	del counts_list[0]	# hack to remove the whitespace key
	return counts_list

def write_counts_file(text_file, counts_list):
	output = open(text_file, 'w')
	output.write('Word' + ' ' * 16 + 'Count\n')
	output.write(len('Word' + ' ' * 16 + 'Count') * '=' + '\n')
	for item in counts_list:
		output.write("%s\t\t%d\n" % (item[0], item[1]))
	output.close()

def get_longest_word(words):
	longest = ''
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest


if __name__ == '__main__':
	text = get_text('alice_in_wonderland.txt')
	check_tuple = get_check_tuple()
	text = filter_words(text, check_tuple)
	text = split_hyphenated_words(text)
	word_counts = get_word_counts({}, text)
	counts_list = get_counts_list(word_counts)
	write_counts_file('alice_words.txt', counts_list)
	longest = get_longest_word(word_counts.keys())
	print 'The longest word is %s with %d characters.' % (longest, len(longest))
