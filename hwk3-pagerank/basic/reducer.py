#!/usr/bin/env python

import sys

# initialize variables 
original, current_key, current_pr = None, None, 0

# process line by line 
for line in sys.stdin:

	# parse key/val pair 
	vals = line.split('\t')
	key, val = vals[0], vals[1] # note val can hold original outlinks OR pr 

	# if still processing same key
	if key == current_key: 

		# special case: if val is the original outlinks info, hold it 
		if 'PR' not in val:
			original = val.strip()

		# else increment pr 
		else: 
			pr = float(val.split(' ')[1])
			current_pr += pr 
	
	# if given new key 
	else:

		# print previous key's info as long as it is not null 
		if current_key is None: 
			pass 
		else: 
			print("%s %s %s" % (current_key, original, str(current_pr))) 

		# process new key  

		if 'PR' not in val:
			original = val.strip()
			current_key, current_pr = key, 0 

		else: 
			pr = float(val.split(' ')[1])
			current_key, current_pr = key, pr 

# handle the last key 
print("%s %s %s" % (current_key, original, str(current_pr)))