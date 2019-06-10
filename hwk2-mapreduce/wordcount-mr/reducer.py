#!/usr/bin/env python

# import libraries 
import re
import sys

# hard code search terms 
SEARCH_TERMS = ['hackathon', 'Dec', 'Chicago', 'Java']

# create dict to hold mapping of lowercase term to original term 
# term_mapping = {ori_term.lower(): ori_term for ori_term in SEARCH_TERMS} # didn't work on dumbo 
term_mapping = dict((ori_term.lower(), ori_term) for ori_term in SEARCH_TERMS)

# initialize variables 
current_word, word_count = None, 0

# process each key/value pair from map output 
for line in sys.stdin: 
	val = line.strip().split("\t")
	norm_term, term_count = val[0], int(val[1])
	# if incoming term is current word, increment word count 
	if norm_term == current_word: 
		word_count += term_count
	# else it must be a new word, and we must have finished the previous word 
	else: 
		# assuming current word is not just initial None, print results of previous word 
		if current_word is not None: 
			print("{}\t{}".format(term_mapping[current_word], word_count)) # convert lowercase term back to original 
		# swap new word as current word and update its count 
		current_word = norm_term
		word_count = term_count

# handle the last key 
print("{}\t{}".format(term_mapping[current_word], word_count)) # convert lowercase term back to original 