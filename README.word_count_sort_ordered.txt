Consider the DNA sequence "AGGCCCTTTT" of length 10.

There are 4 possible characters ['A', 'C', 'T', 'G']

Consider a word size of 2.

Then there are 9 possible words of size 2 assuming a stride of 1 are:

AG
GG
GC
CC
CC
CT
TT
TT
TT

We count how many times each word occurs in the DNA sequence:

{'AA': 0, 
 'AC': 0,
 'GT': 0,
 'AG': 1,
 'CC': 2,
 'CA': 0,
 'CG': 0,
 'TT': 3,
 'GG': 1,
 'GC': 1,
 'AT': 0,
 'GA': 0,
 'TG': 0,
 'TA': 0,
 'TC': 0,
 'CT': 1}

The words are then sorted by the number of times it occurs in the DNA sequence:
('wordes sorted based on count: ', ['TT', 'CC', 'AG', 'GG', 'GC', 'CT', 'AA', 'AC', 'GT', 'CA', 'CG', 'AT', 'GA', 'TG', 'TA', 'TC'])

TT 3
CC 2
AG 1
GG 1
GC 1
CT 1

Finally, the words are converted to an int representing their sort order. When two words have the same count, the sort order is determed by the python sorted function.

TT 3 6
CC 2 5
AG 1 4
GG 1 3
GC 1 2
CT 1 1


 
