#!/usr/bin/env python
"""
	Crack open a Milwaukee's Beast, grab some 
	college rule from your peechee, and jot down
	some song titles for the album of 26 songs that 
	you will spend the thirteen hours recording.

	Examples:
		Adoptee Yengee Permixture Threadlet
		Unplacable Cirri Whitebelly Shockable Antiabsolutist Stippen
		Figured Coracine Mistranslate Physostegia
		Seedman Tauroctonus Nonelementary Antadiform Eureka
		Agatine Sparver
"""

from random import choice
from random import randint

def songtitle(wordcount):
	"""Generates a string of given length (wordcount), using Title Case."""
	title = choice(words).title().strip()
	for i in range(1, wordcount):
		title = title + " " + choice(words).title().strip()
	print title

words = open("/usr/share/dict/words", 'r').readlines()
songtitle(randint(2, 7))
