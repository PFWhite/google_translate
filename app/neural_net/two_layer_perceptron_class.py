import csv
import pandas
import numpy

def sigmoid(x):
    output = 1 / (1 + numpy.exp(-x))
    return output

class Perceptron(object):

    def __init__(self, weights, learning_rate):
        self.weights = weights
        self.learning_rate = learning_rate
#        self.epsilon = epsilon

    def classify(self, inputs):
        #this will do our weights times our input vector
        self.last_input = inputs
        sum = 0
        for index, input in enumerate(inputs):
            sum += self.weights[index] * inputs[index]
        self.o = sigmoid(sum)
#        return self.o

    def update_weights(self, t):
        delta_weight = []
        for index, input in enumerate(self.last_input):
            delta_weight.append(self.learning_rate * (t - self.o) * input)
        # check if within our tolerance for updating weights
#        total_delta = 0
#        for index, delta in enumerate(delta_weight):
#            total_delta += delta
#        if total_delta >= self.epsilon:
        for index, delta in enumerate(delta_weight):
            self.weights[index] += delta

class TLPerceptron(object):

#weights_lower should be a list of initial weight vectors
    def __init__(self, weights_upper, weights_lower, nodes, learning_rate):
        #number of upper weights should be equal to number of nodes plus one for bias
        self.weights_upper = weights_upper
        #number of lower weights should be equal to (#inputs + 1) * (# nodes)
        self.weights_lower = weights_lower
        self.nodes = nodes
        self.learning_rate = learning_rate
#        self.epsilon = epsilon
        self.layers = []
        #layers contains all nodes; last element is the perceptron that actually gives us output
        for iter in range(nodes) :
            self.layers.append(Perceptron(weights_lower[iter], learning_rate))
        self.layers.append(Perceptron(weights_upper, learning_rate))

    def classify(self, inputs):
        self.inputs = inputs
        for iter in range(self.nodes) :
            self.layers[iter].classify(inputs)
        self.hidden_inputs = [1]
        for iter in range(self.nodes) :
            self.hidden_inputs.append(self.layers[iter].o)
        sum = 0
        for index, input in enumerate(self.hidden_inputs):
            sum += self.weights_upper[index] * self.hidden_inputs[index]
        self.o = sigmoid(sum)

    def update_weights(self, t):
        delta_upper_weight = []
        delta_lower_weight = []
        for index, input in enumerate(self.hidden_inputs):
            delta_upper_weight.append(self.learning_rate * (t - self.o) * (1 - self.o) * self.o * input)
        for iter in range(self.nodes):
            temp = []
            for index, input in enumerate(self.inputs):
                temp.append(self.learning_rate * (t - self.o) * (1 - self.o) * self.o *
                            self.weights_upper[iter] * self.hidden_inputs[iter] *
                            (1 - self.hidden_inputs[iter]) * input)
            delta_lower_weight.append(temp)
        for index, delta in enumerate(delta_upper_weight) :
            self.weights_upper[index] += delta
        for iter in range(self.nodes):
            for index, delta in enumerate(delta_lower_weight[iter]):
                self.weights_lower[iter][index] += delta






#data upload
colnames = ['X0', 'X1', 'X2', 'X3', 'Y']
testdata = pandas.read_csv('testdata2.csv')
i = testdata.ix[:,1]
x = testdata.ix[:,2]
y = testdata.ix[:,3]
z = testdata.ix[:,4]
t = testdata.ix[:,5]

#setting initial values for perceptron
wu = [0,0,0,0]
wl = [[1,0,0,0],[0,1,0,0],[0,0,1,0]]
a = 1

#initialize perceptron with 3 hidden layers
p1 = TLPerceptron(wu, wl, 3, a)
X = [i,x,y,z,t]

#running Perceptron update 20 times, saving the outputs of the last time
for j in range(19) :
    for k in range(len(i)) :
        up = [X[0][k], X[1][k], X[2][k], X[3][k]]
        p1.classify(up)
        p1.update_weights(X[4][k])

O = []
for k in range(len(i)) :
    up = [X[0][k], X[1][k], X[2][k], X[3][k]]
    p1.classify(up)
    p1.update_weights(X[4][k])
    O.append(p1.o)

#figuring out where it went wrong
D = []
for k in range(len(O)) :
    D.append(t[k] - float(O[k]))
