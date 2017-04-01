import theano
import theano.tensor as T
import numpy as np

def weight_func(val):
    max_val = 5
    alpha = 1
    return ( val/max_val )** alpha

path = './en/matrix'

M = np.loadtxt(path, dtype='float32')

word_dim = 100
seed = 1

rng = np.random.RandomState(seed)

W = rng.normal(0, 0.1, (10000, word_dim + 1)).astype('float32')
B = rng.normal(0, 0.1, (10000, word_dim + 1)).astype('float32')

epochs = 20
