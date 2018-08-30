
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# load text
raw_text = load_doc('rhyme.txt')
print(raw_text)

# clean You may want to explore other methods for data cleaning, such as normalizing the case to lowercase or removing punctuation in an effort to reduce the final vocabulary size and develop a smaller and leaner model.

tokens = raw_text.split()
raw_text = str.lower(' '.join(tokens))
print (raw_text)

# organize into sequences of characters of length 10. Looks like a sliding window of length 10 and stride of 1.
length = 10
sequences = list()
for i in range(length, len(raw_text)):
	# select sequence of tokens
	seq = raw_text[i-length:i+1]
	# store
	sequences.append(seq)
print(sequences)
print('Total Sequences: %d' % len(sequences))

# save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

# save sequences to file
out_filename = 'char_sequences.txt'
save_doc(sequences, out_filename)
