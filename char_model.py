from numpy import array
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


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
raw_text = load_doc('char_sequences.txt')
lines = raw_text.split('\n')


# encode sequences. mapping just assigns unique ints to each character
chars = sorted(list(set(raw_text)))
mapping = dict((c, i) for i, c in enumerate(chars))

# process each sequence of characters one at a time and use the dictionary mapping to look up the integer value for each character.
sequences = list()
for line in lines:
	# integer encode line
	encoded_seq = [mapping[char] for char in line]
	# store
	sequences.append(encoded_seq)

# vocabulary size
vocab_size = len(mapping)
print('Vocabulary Size: %d' % vocab_size)

# Now that the sequences have been integer encoded, we can separate the columns into input and output sequences of characters.
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]

# one hot encode the input and output sequences
sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)


# define model
model = Sequential()
model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

# The model is learning a multi-class classification problem, therefore we use the categorical log loss intended for this type of problem. The efficient Adam implementation of gradient descent is used to optimize the model and accuracy is reported at the end of each batch update.

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=100, verbose=2)

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=100, verbose=2)

# The Keras model API provides the save() function that we can use to save the model to a single file, including weights and topology information

# save the model to file
model.save('model.h5')

# We also save the mapping from characters to integers that we will need to encode any input when using the model and decode any output from the model.

# save the mapping
dump(mapping, open('mapping.pkl', 'wb'))
