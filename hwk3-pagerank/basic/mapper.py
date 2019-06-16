#!/usr/bin/env python

import sys

for line in sys.stdin: 

	# split input into parent node, outlinks, and pr 
	vals = line.strip().split(' ')
	parent_pr = float(vals.pop())
	parent, outlinks = vals[0], vals[1:]

	# print pr received by each outlink
	for outlink in outlinks:
		print("%s\tPR %s" % (outlink, parent_pr/len(outlinks)))

	# finally also print out the original outlinks info 
	outlinks_val = ' '.join(outlinks)
	print("%s\t%s" % (parent, outlinks_val))