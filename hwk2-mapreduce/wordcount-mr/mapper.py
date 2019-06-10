#!/usr/bin/env python

# import libraries 
import re
import sys

# hard code search terms 
SEARCH_TERMS = ['hackathon', 'Dec', 'Chicago', 'Java']

# create dict to hold mapping of lowercase term to original term 
term_mapping = {ori_term.lower(): ori_term for ori_term in SEARCH_TERMS}

# process each line with hadoop streaming 
for line in sys.stdin:
	val = line.strip()
	words = [w for w in re.split('\W+', val.lower())] # split line into words 

	# iterate through each search term and check whether term is in words 
	for term in term_mapping.keys():
		if term in words: 
			print("{}\t{}".format(term, 1))
		else: 
			print("{}\t{}".format(term, 0))
