# purpose: to scale word vectors to be between (0, 1), not inclusive

import numpy as np

# limits output to 5 decimals and suppresses scientific notation
np.set_printoptions(precision=5, suppress=True)


vocab_size = 10
word_vec_length = 5

rand_int_lower = -10
rand_int_upper = 10

# sigmoid function has horizontal asymptotes at 0 and 1, so we don't want 0 or 1 to ever occur exactly in our word vectors
epsilon = .0001

# generates word vectors as random floats between [-10, 10)
word_vecs = (rand_int_upper - rand_int_lower) * np.random.random(size = (vocab_size,word_vec_length)) + rand_int_lower

print("original word_vecs:", "\n", word_vecs)

# first, find the smallest value (ie the most negative) in the matrix
smallest_entry = rand_int_upper

for word_index, word_vec in enumerate(word_vecs):
    # word_vec_col gives the entry for word_vecs[word_index, col_index]
    for col_index, word_vec_col in enumerate(word_vec):
        if (word_vec_col < smallest_entry):
            smallest_entry = word_vec_col

# next, find the largest value (ie the most positive) in the matrix
largest_entry = rand_int_lower

for word_index, word_vec in enumerate(word_vecs):
    # word_vec_col gives the entry for word_vecs[word_index, col_index]
    for col_index, word_vec_col in enumerate(word_vec):
        if (word_vec_col > largest_entry):
            largest_entry = word_vec_col

# next, shift all entries up to make the smallest entry greater than 0
# add the opposite of the smallest entry (plus a multiplier of epsilon) to all entries in the matrix to shift
for word_index, word_vec in enumerate(word_vecs):
    # word_vec_col gives the entry for word_vecs[word_index, col_index]
    for col_index, word_vec_col in enumerate(word_vec):
        word_vec_col = word_vec_col - smallest_entry + (epsilon * (1 + largest_entry))
        word_vecs[word_index, col_index] = word_vec_col

# next, find the new largest value (ie the most positive) in the matrix, after shifting
new_largest_entry = 0

for word_index, word_vec in enumerate(word_vecs):
    # word_vec_col gives the entry for word_vecs[word_index, col_index]
    for col_index, word_vec_col in enumerate(word_vec):
        if (word_vec_col > new_largest_entry):
            new_largest_entry = word_vec_col

# next, scale all entries up to make the largest entry less than 1
# subtract epsilon from all entries
# then divide all entries by the new largest entry in the matrix to scale
for word_index, word_vec in enumerate(word_vecs):
    # word_vec_col gives the entry for word_vecs[word_index, col_index]
    for col_index, word_vec_col in enumerate(word_vec):
        word_vec_col = word_vec_col - epsilon
        word_vec_col = word_vec_col / new_largest_entry
        word_vecs[word_index, col_index] = word_vec_col

print("\n", "word_vecs - shifted and scaled to (0,1):", "\n", word_vecs)
