from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

# load the model
model = load_model('model.h5')

# load the mapping
mapping = load(open('mapping.pkl', 'rb'))


def generate_seq(model, mapping, seq_length, seed_text, n_chars):
    # A given input sequence will need to be prepared in the same way 
    # as preparing the training data for the model.

    # encode the characters as integers
    in_text = str.lower(seed_text)

    # generate a fixed number of characters
    for _ in range(n_chars):

        encoded = [mapping[char] for char in in_text]
        print (encoded)

        # truncate sequences to a fixed length
        encoded = encoded[-seq_length:]
        # one hot encode
        encoded = to_categorical(encoded, num_classes=len(mapping))
        encoded = encoded.reshape(1, encoded.shape[0], encoded.shape[1])

        # We use predict_classes() instead of predict() to directly 
        # select the integer for the character with the highest probability
        # instead of getting the full probability distribution across 
        # the entire set of characters.

        # predict character
        yhat = model.predict_classes(encoded, verbose=0)

        # We can then decode this integer by looking up the mapping to 
        # see the character to which it maps.

        out_char = ''
        for char, index in mapping.items():
            if index == yhat:
                out_char = char
                break

        print(out_char)
        in_text += char
    return in_text


print(generate_seq(model, mapping, 10, 'Sing a son', 40))
