import sys
import itertools
from operator import itemgetter

def read_from_file(fname):
	f = open(fname)
	s = f.read()
	f.close
	return s.upper().rstrip()


# count occurrances of 1 char words
# takes as input a dictionary of word counts
# returns a dictionary of word counts
# def count_occurance(s):
# 	dc = dict((char_, 0) for char_ in set(s))
# 	for char_ in set(s):
# 		dc[char_] = dc[char_] + s.count(char_)
# 	return dc
def count_occurance(s, n=1):
	print "set: ", set(s)
	dc = dict((''.join(char_), 0) 
				for char_ in itertools.product(set(s), repeat=n)
			 )
	for char_ in itertools.product(set(s), repeat=n):
		char = ''.join(char_)
		dc[char] = dc[char] + occurrences(s, char)
        dc = { k:v for k, v in dc.items() if v }
	return dc

# helper sub because string.count(ss) counts non-overlapping
# occurrences of substring in string
def occurrences(string, sub):
	count = start = 0
	while True:
		start = string.find(sub, start) + 1
		if start > 0:
			count+=1
		else:
			return count


# sort words based on count
# takes as input a dictionary of word counts
# returns an array of count sorted words highest count first
def count_ordered(dc):
    # get rid of k:v pairs where v is 0
    dc = { k:v for k, v in dc.items() if v }
    ds=sorted(dc, key=dc.get, reverse=True)
    return ds


# assingn integer value to each word based on count order
# takes as input a string of words and an array of words
# returns 
def word_to_int(s, csw, n=1):
	dsn = { c : i+1 for i, c in enumerate(csw)}
	if(n==1):
		return map (lambda x : dsn[x] , s)
	if(n==2):
		return map (lambda x : dsn[''.join(x)] , zip(s[::1],s[1::1]))
	if(n==3):
		return map (lambda x : dsn[''.join(x)] , zip(s[::1],s[1::1],s[2::1]))
	if(n==4):
		return map (lambda x : dsn[''.join(x)] , zip(s[::1],s[1::1],s[2::1],s[3::1]))

# map takes a function and a list and applies function
# to all elements of the list.

### Main Test ###
if (len(sys.argv) != 3):
	print 'requires arg1=string'
	print 'requires arg2=word size'
	sys.exit(1)


s = read_from_file(sys.argv[1])
print(s)
n = int(sys.argv[2])

# count occurrances of n char words
dc = count_occurance(s, n)
print "dc: ", dc

# sort words based on count
csw = count_ordered(dc)
print ("wordes sorted based on count: ", csw)

dc_size = len(dc)
for k, v in sorted(dc.items(), key=itemgetter(1), reverse=True):
    print k, v, dc_size
    dc_size = dc_size - 1

# word to count ordered int
i = word_to_int(s, csw, n) 

# print 'set in s: ', list(set(s))
# print 'counts:   ', dc
# print 'count_ordered', csw

print 'set in s: ', list(set(s))
print s
print i

