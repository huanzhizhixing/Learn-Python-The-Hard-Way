# -*- coding: utf-8 -*-

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words and then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	


"""
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words=ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sorted_words' is not defined
>>> sort_words
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sort_words' is not defined
>>> sort_words = ex25.sort_words(words)
>>> sorted_words
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sorted_words' is not defined
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> wrods
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wrods' is not defined
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_word)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sorted_word' is not defined
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>>
"""




