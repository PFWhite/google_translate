import numpy
import math
import random

def sigmoid(x):
    return 1/(1 + math.exp(-x))

class PerceptronSigmoid(object):

#weights should be a numpy.array object
    def __init__(self, weights, learning_rate):
        self.weights = weights
        self.learning_rate = learning_rate

#inputs should be a numpy.array object
    def classify(self, inputs):
        #this will do our weights times our input vector
        self.last_input = inputs
        sum = numpy.dot(self.weights, inputs)
        self.o = sigmoid(sum)

    def update_weights(self, t):
        delta_weight = self.learning_rate * (t - self.o) * self.o * (1 - self.o) * self.last_input
        self.weights += delta_weight


#This initially was going to let the width be generic, but it's turning out too annoying to specify structure. This script uses width=3.
#Looks at the jth element, the j-1th element, and the j+1th element. 
class CNN(object):

    def __init__(self, weights_upper, weights_lower, num_nodes_lower, num_nodes_upper, learning_rate):
        #upper weights should have (#outputs) elements, each with (#inputs) + 1 weights
        self.weights_upper = weights_upper
        #number of lower weights should be equal to width + 1
        self.weights_lower = weights_lower
        #num_nodes_lower should be number of inputs
        self.num_nodes_lower = num_nodes_lower
        #num_nodes_upper should be number of outputs
        self.num_nodes_upper = num_nodes_upper
        self.learning_rate = learning_rate
        self.width = 3
        self.con_layer = []
        for iter in range(num_nodes_lower):
            self.con_layer.append(PerceptronSigmoid(weights_lower, learning_rate))
        self.upper_layer = []
        for iter in range(num_nodes_upper):
            self.upper_layer.append(PerceptronSigmoid(weights_upper[iter], learning_rate))

    def classify(self, inputs):
        self.inputs = numpy.array([float(0)])
        for k in range(len(inputs)):
            self.inputs = numpy.append(self.inputs, inputs[k])
        self.inputs = numpy.append(self.inputs, float(0))
        for iter in range(self.num_nodes_lower):
            temp = numpy.array([float(1)])
            temp = numpy.append(temp, self.inputs[iter:(iter+self.width)])
            self.con_layer[iter].classify(temp)
        self.con_out = numpy.array([])
        for iter in range(self.num_nodes_lower):
            self.con_out = numpy.append(self.con_out, self.con_layer[iter].o)
        temp = numpy.array([float(1)])
        temp = numpy.append(temp, self.con_out)
        for iter in range(self.num_nodes_upper):
            self.upper_layer[iter].classify(temp)
        self.o = numpy.array([])
        for iter in range(self.num_nodes_upper):
            self.o = numpy.append(self.o, self.upper_layer[iter].o)

    def update_weights(self, t):
        delta_lower = numpy.zeros(self.width + 1)
        for j in range(self.num_nodes_lower):
            for i in range(self.num_nodes_upper):
                delta_lower[0] += self.learning_rate * (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i]) * self.weights_upper[i][j] * self.con_layer[j].o * (1 - self.con_layer[j].o)
        for j in range(self.num_nodes_lower):
            for i in range(self.num_nodes_upper):
                delta_lower[1] += self.learning_rate * (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i]) * self.weights_upper[i][j] * self.con_layer[j].o * (1 - self.con_layer[j].o) * p1.inputs[j]
        for j in range(self.num_nodes_lower):
            for i in range(self.num_nodes_upper):
                delta_lower[2] += self.learning_rate * (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i]) * self.weights_upper[i][j] * self.con_layer[j].o * (1 - self.con_layer[j].o) * p1.inputs[j+1]
        for j in range(self.num_nodes_lower):
            for i in range(self.num_nodes_upper):
                delta_lower[3] += self.learning_rate * (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i]) * self.weights_upper[i][j] * self.con_layer[j].o * (1 - self.con_layer[j].o) * p1.inputs[j+2]
        for j in range(self.width + 1):
            self.weights_lower[j] += delta_lower[j]
        for i in range(self.num_nodes_upper):
            delta_upper = numpy.zeros(len(self.weights_upper[i]))
            delta_upper[0] += self.learning_rate *  (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i])
            for j in range(self.num_nodes_lower):
                delta_upper[j+1] += self.learning_rate *  (t[i] - self.o[i]) * self.o[i] * (1 - self.o[i]) * self.con_out[j]
            for j in range(len(delta_upper)):
                self.weights_upper[i][j] += delta_upper[j]

