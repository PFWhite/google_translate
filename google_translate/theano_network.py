import random
from copy import copy

import theano
from theano import tensor as T
from theano import function

import numpy as np


class Network(object):

    def __init__(self, network_config, path):
        self.config = copy(network_config)

        self.data = T.matrix('data')

        self.encoder = T.matrix('encode')
        self.decoder = T.matrix('decode')

        code = T.dot(self.data, self.encoder)

        s_code = 1 / (1 + T.exp(-code))

        decode = T.dot(s_code, self.decoder)

        s_decode = 1 / (1 + T.exp(-decode))

        self.encode = function([ self.data, self.encoder ], s_code)
        self.decode = function([ s_code, self.decoder ], s_decode)


    def train(self, data, epochs):
        for epoch in range(0, epochs):
            code = self.encode(data, self.encoder)
            out = self.decode(code, self.decoder)
        self.backpropagate(out, data)


    def backpropagate(self, output, target):
        pass
