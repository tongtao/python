# -*- coding: utf-8 -*-

#Even More Practice
#ex25.py

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentrnce)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentrnce(sentence)
	print_first_word(words)
	print_last_word(words)

#help(ex25) and also help(ex25.break_words), 
#	you can get the special strings called documentation comments

#Try breaking your file and see what it looks like in Python when you use it. 
#	You will have to quit Python with CTRL-D (CTRL-Z on windows) to be able to reload it.