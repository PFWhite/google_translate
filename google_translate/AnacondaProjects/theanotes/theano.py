#!/home/patrick/anaconda3/bin/python
import numpy as np
import theano
import theano.tensor as T

def relu(matrix):
    return T.switch(matrix<0, 0, matrix)

rng = np.random.RandomState(42)

indim = 3
outd = 1

sigma = 0.01
mean = 0
node_num = 4

layer1 = theano.shared(rng.normal(mean, sigma, (indim + 1, node_num)), name='hidden_layer')
layer2 = theano.shared(rng.normal(mean, sigma, (node_num + 1, outd)), name='out_layer')

# data = np.loadtxt('./datafile')
print(layer1)
print(layer2)

